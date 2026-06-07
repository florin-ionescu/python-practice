#Inheritance (moștenirea) în Python este un concept OOP prin care o clasă poate prelua (moșteni) atribute și metode de la o altă clasă.
#Parent class → Child class // The child gets everything from the parent.

class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):

    def bark(self):
        print("Dog barks")

dog = Dog()

dog.speak()
dog.bark()


class MartialArts():
    def __init__(self):
        pass


class Aikido(MartialArts):
    def __init__(self):
        pass
