"""
os module

What it does:
- Interacts with the operating system.
- Useful for folders, paths, environment variables, and file checks.
"""
import os

# Get current working directory
current_dir = os.getcwd()
print("Current directory:", current_dir)

# List files and folders
items = os.listdir(".")
print("Items in current folder: ", items)

# Create a folder
if not os.path.exists("reports"):
    os.mkdir("reports")
    print("Folder created")

# Check if a file exists
if os.path.exists("employees.csv"):
    print("employees.csv exists")
else:
    print("Doesnt exist")

# Rename a file
# os.rename("old_name.txt", "new_name.txt")

#r Remove a file
# os.remove("file_to_delete.txt")

# Environment variable example
home_dir = os.environ.get("HOME")
print("Home dir: ", home_dir)
# Environment variables are useful for storing paths, usernames, tokens, and configuration values.