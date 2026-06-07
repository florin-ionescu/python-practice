"""
Polymorphism in Python is the ability for different objects or classes to be used through the same interface, 
even though they behave differently internally.
The word comes from Greek:

poly = many
morph = forms

So polymorphism means “many forms.”
"""

class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())

'''
Both Dog and Cat have a speak() method, but each behaves differently.
The loop does not care what type the object is — it just calls speak(). That is polymorphism.
'''

"""
Types of Polymorphism in Python
1. Method Overriding (Runtime Polymorphism) - A child class provides its own implementation of a parent class method.
2. Duck Typing - Python cares more about what an object can do than its actual type. “If it looks like a duck and quacks like a duck, it’s a duck.”
3. Operator Polymorphism - Operators behave differently depending on the data type.

Why Polymorphism is Useful

Polymorphism helps make code:

* More flexible
* Easier to extend
* Cleaner and reusable
* Less dependent on specific classes

Instead of writing separate code for every type, you write general code that works with many objects.
"""

