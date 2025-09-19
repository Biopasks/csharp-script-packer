# C# Script Packer

A simple Python script to combine all C# (.cs) files from a directory (e.g., Unity project) into a single text file, grouped by folders with ASCII separators. Includes encoding detection and error logging.

## Features
- Recursively scans directories.
- Groups files by folders with separators.
- Auto-detects file encoding using `chardet`.
- Logs errors to a separate file.
- CLI support for flexible usage.

## Requirements
- Python 3.6+
- `chardet` (`pip install chardet`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Biopasks/csharp-script-packer.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script with the path to the directory containing C# files:
```bash
python pack_csharp_scripts.py /path/to/source/dir --output_file output.txt --log_file errors.log
```
- `source_dir`: Path to the directory with C# scripts (required).
- `--output_file`: Output file name (default: `combined_csharp_scripts_with_folders.txt`).
- `--log_file`: Log file name (default: `pack_errors.log`).

### Example
For a Unity project folder:
```bash
python pack_csharp_scripts.py "Assets/Scripts"
```
Output: `output.txt` with all .cs files' code and `errors.log` with any errors.

## License
MIT License. See [LICENSE](LICENSE).

## Contributing
Pull requests are welcome! Format code with Black (`black pack_csharp_scripts.py`) before submitting.
