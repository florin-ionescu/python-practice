"""
requests

What it does:
- Sends HTTP requests.
- Useful for API testing and automation.
- Common methods: GET, POST, PUT, PATCH, DELETE.
"""
import requests

# GET  - Retrieve data from an API.
response = requests.get("https://reqres.in/api/users/2")
print("Status code:", response.status_code)
print("Response body:", response.json())

# Check if request was successful
if response.status_code ==200:
    print("Success")
else:
    print("Request failed")

# POST request
payload = {
    "name": "Florin",
    "job": "QA"
}

response = requests.post("https://reqres.in/api/users", json=payload)
print("Status code:", response.status_code)
print("Response body:", response.json())

# Headers example
headers = {
    "Content-Type": "appplication/json"
}

response = requests.get(
    "https://reqres.in/api/users",
    headers=headers,
    params={"page": 2}
)
print(response.json())

'''
200 = OK
201 = Created
204 = No Content
400 = Bad Request
401 = Unauthorized
403 = Forbidden
404 = Not Found
500 = Server Error
'''