"""
MATCH CASE IN PYTHON

match case was introduced in Python 3.10.

It is similar to switch/case from other programming languages.

It is used when you want to compare one value against multiple possible cases.

Syntax:

match value:
    case option1:
        code
    case option2:
        code
    case _:
        default code

The underscore _ means default case.
"""

# Basic example
status_code = 400
match status_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 400:
        print("bad request")
    case 401:
        print("Unauthorized")
    case 404:
        print("Not found")
    case 500:
        print("Server error")
    case _:
        print("Unknown status code")


# Example with strings
ticket_priority = "high"

match ticket_priority:
    case "low":
        print("Handle when possible")
    case "medium":
        print("Normal queue")
    case "high":
        print("Prioritize")
    case _:
        print("Unknown priority")

# Multiple values in one case
day = "Saturday"
match day:
    case "Saturday" | "Sunday":
        print("weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Unknown day")


# Matching with conditions
score = 85



"""
WHEN TO USE MATCH CASE

Use match case when:
- you compare one value against many possible options
- you want cleaner code than many elif statements
- you work with commands, statuses, roles, or response codes

Examples:
- API status code handling
- ticket priority handling
- command-line menu options
- user role permissions
- application states


WHEN NOT TO USE MATCH CASE

Do not use match case when:
- you only have one or two conditions
- you need complex boolean logic
- simple if / elif / else is easier to read
"""