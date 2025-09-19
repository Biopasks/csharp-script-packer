import os

def create_gitignore():
    """Create .gitignore file."""
    content = """__pycache__/
*.pyc
*.log
*.txt
"""
    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write(content)
    print("Created .gitignore")

def create_requirements():
    """Create requirements.txt file."""
    content = "chardet\n"
    with open("requirements.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("Created requirements.txt")

def create_license(author_name):
    """Create MIT License file."""
    content = f"""MIT License

Copyright (c) 2025 {author_name}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    with open("LICENSE", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created LICENSE (author: {author_name})")

def create_readme(github_username):
    """Create README.md file."""
    content = f"""# C# Script Packer

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
   git clone https://github.com/{github_username}/csharp-script-packer.git
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
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created README.md (username: {github_username})")

def create_github_actions():
    """Create GitHub Actions workflow for linting."""
    os.makedirs(".github/workflows", exist_ok=True)
    content = """name: Lint
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install black pylint
      - name: Run Black
        run: black --check .
      - name: Run Pylint
        run: pylint pack_csharp_scripts.py
"""
    with open(".github/workflows/lint.yml", "w", encoding="utf-8") as f:
        f.write(content)
    print("Created .github/workflows/lint.yml")

def main():
    # Hardcoded for simplicity; replace with your details
    author_name = "Sanot"  # Замени на своё имя или ник
    github_username = "Biopasks"  # Замени на свой GitHub-юзернейм
    
    create_gitignore()
    create_requirements()
    create_license(author_name)
    create_readme(github_username)
    create_github_actions()
    
    print("All files created! Check the current directory.")

if __name__ == "__main__":
    main()
 