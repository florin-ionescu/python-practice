"""
subprocess module

What it does:
- Runs terminal commands from Python.
- Useful for automation scripts, checking system commands, Git commands, tests, etc.
"""
import subprocess
'''
Useful for automation:
run pytest
run git commands
check Python version
call scripts
run operating system commands
'''

# Run a simple command
result = subprocess.run(
    ["cmd", "/c", "echo", "Hello from subprocess"],
    # Captures the command output so you can use it in Python.
    capture_output=True,
    # text=True return the output as text instead of bytes
    text=True
)
'''
cmd = Windows command shell
/c = run the command and then close
echo = command executed inside CMD
'''

print("Output:", result.stdout)
print("Return code:", result.returncode)

# Run command and check output
result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)
print("Python version:", result.stdout)

# Example with error handling
try:
    result = subprocess.run(
        ["python", "--ersion"],
        capture_output=True,
        text=True,
        check=True
    )
    print(result.stdout)
except subprocess.CalledProcessError as error:
    print("Command failed")
    print(error)
