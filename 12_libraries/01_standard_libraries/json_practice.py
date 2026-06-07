"""
json module

What it does:
- Reads and writes JSON data.
- JSON is commonly used in APIs.
- Useful when testing REST APIs or saving structured data.
"""
import json

# Python dictionary
user = {
    "name": "Florin",
    "role": "IT Support",
    "skills": ["Python", "SQL", "Linux"]
}

# Convert Python dict to JSON string
json_text = json.dumps(user, indent=4) # indent 4 makes it easier to read
# dumps means “dump to string”.
print(json_text)

# Convert JSON string back to python dict
converted_user = json.loads(json_text)
# loads means “load from string”. Converts back to dict
print(converted_user["name"])
print(converted_user["skills"])


# Write JSON to file
with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

# Read JSON from file
with open("user.json", "r") as file:
    data = json.load(file)
print(data)