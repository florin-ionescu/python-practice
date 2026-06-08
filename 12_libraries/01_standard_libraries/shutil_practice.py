"""
shutil module

What it does:
- Performs high-level file operations.
- Useful for copying, moving, deleting folders, and archiving files.
"""
import shutil
'''shutil is used for high-level file operations.
copying files
moving files
copying folders
deleting folders
creating zip archives
'''
from pathlib import Path

# Create sample file
source = Path("sample.txt")
source.write_text("This is a sample file.")

# Copy file
destination = Path("sample_copy.txt")
shutil.copy(source, destination)
print("File copied")

# Create folder
backup_folder = Path("backup")
backup_folder.mkdir(exist_ok=True)

# Move file into folder
shutil.move("sample_copy.txt", backup_folder / "sample_copy.txt")
print("File moved")

# Copy entire folder
# shutil.copytree("backup", "backup_copy")

# Delete folder and everything inside it
# shutil.rmtree("backup")

# Create archive
# shutil.make_archive("backup_archive", "zip", "backup")

