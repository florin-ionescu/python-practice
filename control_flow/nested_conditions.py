# Nested conditions means putting an if statement inside another if statement.

age = 18
has_id = False

if age >= 18:
    # So the inner condition only runs if the outer condition is true.
    if has_id:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote!")
else:
    print("You are too young to vote!")

