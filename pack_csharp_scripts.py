#!/usr/bin/env python3
import os
import chardet
import argparse

# ASCII separators
folder_separator = f"\n{'='*80}\n"
file_separator = f"\n{'-'*80}\n"

def detect_encoding(file_path):
    """Detect the encoding of a file."""
    try:
        with open(file_path, "rb") as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            return result["encoding"] if result["encoding"] else "utf-8"
    except Exception:
        return "latin1"

def pack_scripts_with_folders(source_dir, output_file, log_file):
    """Pack all C# scripts from a directory into a single text file with folder structure."""
    cs_files = []
    
    # Walk through all subdirectories, handling access errors
    for root, dirs, files in os.walk(source_dir, onerror=lambda err: print(f"Access error: {err}")):
        for file in files:
            if file.lower().endswith('.cs'):  # Case-insensitive extension check
                full_path = os.path.join(root, file)
                cs_files.append(full_path)
    
    if not cs_files:
        print("No C# scripts found!")
        with open(log_file, "w", encoding="utf-8") as log:
            log.write("Error: No .cs files found\n")
        return

    # Print the list of found files for diagnostics
    print(f"Found {len(cs_files)} .cs files:")
    for f in sorted(cs_files):
        print(f)

    # Sort files by directory for grouping
    cs_files.sort(key=lambda x: os.path.dirname(x))
    
    processed_files = 0
    with open(output_file, "w", encoding="utf-8") as outfile, open(log_file, "w", encoding="utf-8") as log:
        current_folder = None
        for file_path in cs_files:
            rel_path = os.path.relpath(file_path, source_dir).replace('\\', '/')  # Normalize slashes
            folder = os.path.dirname(rel_path)
            file_name = os.path.basename(file_path)
            full_path = file_path.replace('\\', '/')  # Full path for output
            
            # New folder
            if folder != current_folder:
                outfile.write(f"{folder_separator}FOLDER: {folder or 'Root'} (Full Path: {os.path.dirname(file_path).replace('\\', '/')})\n{folder_separator}")
                log.write(f"Added folder: {folder or 'Root'} (Full Path: {os.path.dirname(file_path).replace('\\', '/')})\n")
                current_folder = folder
            
            # Write file with full path
            outfile.write(f"{file_separator}FILE: {file_name} (Full Path: {full_path})\n{file_separator}")
            try:
                encoding = detect_encoding(file_path)
                with open(file_path, "r", encoding=encoding, errors="ignore") as infile:  # Ignore encoding errors
                    content = infile.read()
                    outfile.write(content + "\n")
                log.write(f"Success: {file_path} (encoding: {encoding})\n")
                processed_files += 1
            except Exception as e:
                log.write(f"Error in {file_path}: {str(e)}\n")
                print(f"Error in {file_path}: {str(e)}")
                outfile.write(f"// Read error: {str(e)}\n")
        
        outfile.write(folder_separator)
    
    print(f"Scripts packed into {output_file}. Processed: {processed_files}/{len(cs_files)}. Log: {log_file}.")
    if processed_files < len(cs_files):
        print("Warning: Not all files were processed successfully. Check the log.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pack C# scripts from a directory into a single text file with folder structure.")
    parser.add_argument("source_dir", type=str, help="Path to the source directory with C# scripts.")
    parser.add_argument("--output_file", type=str, default="combined_csharp_scripts_with_folders.txt", help="Output file name.")
    parser.add_argument("--log_file", type=str, default="pack_errors.log", help="Log file name.")
    
    args = parser.parse_args()
    pack_scripts_with_folders(args.source_dir, args.output_file, args.log_file)
