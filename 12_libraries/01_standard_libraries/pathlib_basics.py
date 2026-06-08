"""
pathlib module

What it does:
- Modern way to work with file and folder paths.
- Easier and cleaner than using strings for paths.
"""
# pathlib is a modern way to work with file paths.
from pathlib import Path

# Current folder
current_path = Path.cwd()
print("Current path:", current_path)

# Create a path to a file
file_path = Path("reports") / "summary.txt"
print(file_path)

# Create folder if it does not exist
folder = Path("reports")
folder.mkdir(exist_ok=True)

# Write text to file: Creates the file if it does not exist:
file_path.write_text("This is a basic report")

# Read txt from file
content = file_path.read_text()
print(content)

# Check if file exists
if file_path.exists():
    print("File exists")

# Get file name and extension
print("File name:", file_path.name)
print("File extension:", file_path.suffix)
print("Parent folder:", file_path.parent)

# List all .txt files in current folder
for file in Path(".").glob("*.txt"):
    # glob() searches for files that match a pattern.
    print(file)