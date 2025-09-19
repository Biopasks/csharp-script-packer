import os
import chardet

# Путь к папке с C# скриптами
source_dir = r"C:\Users\Solana\My project\Assets\Game Kit Controller\Scripts"
output_file = "combined_csharp_scripts_with_folders.txt"
log_file = "pack_errors.log"

# ASCII-разделители
folder_separator = f"\n{'='*80}\n"
file_separator = f"\n{'-'*80}\n"

def detect_encoding(file_path):
    """Определяет кодировку файла."""
    try:
        with open(file_path, "rb") as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            return result["encoding"] if result["encoding"] else "utf-8"
    except:
        return "latin1"

def pack_scripts_with_folders():
    cs_files = []
    
    # Обход всех подпапок с обработкой ошибок доступа
    for root, dirs, files in os.walk(source_dir, onerror=lambda err: print(f"Ошибка доступа: {err}")):
        for file in files:
            if file.lower().endswith('.cs'):  # Игнорируем регистр расширения
                full_path = os.path.join(root, file)
                cs_files.append(full_path)
    
    if not cs_files:
        print("Не найдено C# скриптов!")
        with open(log_file, "w", encoding="utf-8") as log:
            log.write("Ошибка: Не найдено .cs файлов\n")
        return

    # Выводим список найденных файлов для диагностики
    print(f"Найдено {len(cs_files)} .cs файлов:")
    for f in sorted(cs_files):
        print(f)

    # Сортируем файлы по директории для группировки
    cs_files.sort(key=lambda x: os.path.dirname(x))
    
    processed_files = 0
    with open(output_file, "w", encoding="utf-8") as outfile, open(log_file, "w", encoding="utf-8") as log:
        current_folder = None
        for file_path in cs_files:
            rel_path = os.path.relpath(file_path, source_dir).replace('\\', '/')  # Нормализуем слеши
            folder = os.path.dirname(rel_path)
            file_name = os.path.basename(file_path)
            full_path = file_path.replace('\\', '/')  # Полный путь для вывода
            
            # Новая папка
            if folder != current_folder:
                outfile.write(f"{folder_separator}FOLDER: {folder or 'Root'} (Full Path: {os.path.dirname(file_path).replace('\\', '/')})\n{folder_separator}")
                log.write(f"Добавлена папка: {folder or 'Root'} (Full Path: {os.path.dirname(file_path).replace('\\', '/')})\n")
                current_folder = folder
            
            # Пишем файл с полным путем
            outfile.write(f"{file_separator}FILE: {file_name} (Full Path: {full_path})\n{file_separator}")
            try:
                encoding = detect_encoding(file_path)
                with open(file_path, "r", encoding=encoding, errors="ignore") as infile:  # Игнорируем ошибки кодировки
                    content = infile.read()
                    outfile.write(content + "\n")
                log.write(f"Успешно: {file_path} (кодировка: {encoding})\n")
                processed_files += 1
            except Exception as e:
                log.write(f"Ошибка в {file_path}: {str(e)}\n")
                print(f"Ошибка в {file_path}: {str(e)}")
                outfile.write(f"// Ошибка чтения: {str(e)}\n")
        
        outfile.write(folder_separator)
    
    print(f"Скрипты упакованы в {output_file}. Обработано: {processed_files}/{len(cs_files)}. Лог: {log_file}.")
    if processed_files < len(cs_files):
        print("Внимание: Не все файлы были обработаны успешно. Проверьте лог.")

if __name__ == "__main__":
    pack_scripts_with_folders()
