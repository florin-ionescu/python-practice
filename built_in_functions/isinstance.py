# Better than type() for validation.

amount = 100
if isinstance(amount, int):
    print("Amount is an integer")

def add_expense(amount):
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number")
    prin(f"Added expense: {amount}")