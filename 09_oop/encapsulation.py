# Encapsulation in Python

"""Encapsulation is the concept of building data and methods together inside a class and
restricting direct access to some details of an object
It helps protect the internal state of an object from unintended modification.
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(1000)
account.deposit(100)
print(account.balance

"""
* balance is data
* deposit() is behavior

Both are bundled together inside the BankAccount class.

That is encapsulation.
Without encapsulation, anyone could directly modify important data incorrectly.
Encapsulation helps control access to data.

Encapsulation provides:
* Data protection
* Better control over object state
* Cleaner code
* Easier maintenance
* Flexibility to change implementation later
"""
