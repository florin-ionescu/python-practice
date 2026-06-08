"""
python-dotenv

What it does:
- Loads environment variables from a .env file.
- Useful for secrets like API keys, usernames, passwords, tokens.
- Never commit real secrets to GitHub.
"""
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Example .env file:
# API_KEY=123456
# USERNAME=florin

api_key = os.getenv("API_KEY")
username = os.getenv("USERNAME")

print("API Key:", api_key)
print("Username:", username)

# Example check
if api_key:
    print("API key loaded successfully")
else:
    print("API key not found")