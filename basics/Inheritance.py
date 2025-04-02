class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        
        # Calls the parent constructor
        # you can get away by not calling it, but it is best to include it
        super().__init__(name)
        self.age = age

    def info(self):
        return f"{self.name} is {self.age} years old"

    # add a single _ to make it protected
    def _protected_method(self):
        print("I am a protected method")

    # add two __ to make it private
    def __private_method(self):
        print("I am a private method")

# you can inherit from multiple parens this way too
class GrandChild(Child, Parent):

    # this calls the constructors of the parent calsses
    def __init__(self, name, age):
        Child.__init__(self, name, age)
        Parent.__init__(self, name)

    # override works as expected
    def info(self):
        print("I just did an override")

    def scope_method(self):
        self._protected_method()
        self.__private_method()

def test_inheritance_1():

    c1 = Child("Jane", 12)

    print(c1.greet())
    print(c1.info())

    g1 = GrandChild("John", 52)
    print(g1.greet())
    g1.info()

    #isinstance() and issubclass()
    #Check relationships between objects and classes.
    print(isinstance(c1, Child)) 
    print(issubclass(Child, Parent))

    g2 = GrandChild("Michael", 31)
    g2.scope_method()


class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):  # Overriding
        return "Woof!"

class Cat(Animal):
    def make_sound(self):  # Overriding
        return "Meow!"

def animal_sound(animal):  # Works for any class with a speak() method
    return animal.make_sound()

def test_poly_1():
    # Using polymorphism
    animals = [Dog(), Cat(), Animal()]
    for animal in animals:
        print(animal.make_sound())

    # Python doesn’t care if animal is a Dog or Cat—as long
    # as it has a make_sound() method, it works.
    print(animal_sound(Dog()))  # Woof!
    print(animal_sound(Cat()))  # Meow!


