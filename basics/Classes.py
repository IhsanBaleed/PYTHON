# self refers to an instace
# cls refers to the class
# @classmethod and @staticmethod are used to define methods in a class that aren’t regular instance methods


class Person:

    # this is a class variable, similar to static
    COUNTER = 0

    # the constructor
    # we cant define multiple constructors, we can use default arguments to get the same result
    # you can also use class methods (similar to static) to construct an object
    def __init__(self, id_val = 0, age = 0, name = "", weight = 0):
        self.id_ = id_val
        self.age_ = age
        self.name_ = name
        self.weight_ = weight

        # to access a class variable, you must provide the class's name first
        Person.COUNTER += 1

    # all methods of the class must have self as first param
    # this allows the methods to access the content of the class
    def print_info(self):
        print(f" Details are {self.id_} {self.name_} {self.age_} {self.weight_}")

    def class_method():
        print ("I am class method")

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # destructor
    def __del__(self):
        print(f"Deleting {self.make} {self.model}")

    @classmethod # you need to have @classmethod, can be used as an alternative constructor
    def from_string(cls, car_str):
        """Alternative constructor that initializes an object from a string"""
        make, model, year = car_str.split("-")
        return cls(make, model, int(year))  # Creates an instance using cls

    @staticmethod
    def static_method(make, model, year):
        return Car(make, model, year)

    # used to print the object when calling printf
    def __str__(self): # used to print objects normally
        return f"The car is {self.make} {self.model}"  
    def __repr__(self): # used for debugging mainly
        return f"Car('{self.make}', '{self.model}')"

class OperatorLoading:
    
    def __init__(self, name, id_val):
        self.name = name
        self.id = id_val

    # this is operator overloading
    # you can overload many more operators, similar to C++
    def __add__(self, other):
        return OperatorLoading (f"{self.name}  {other.name}", self.id + other.id)


def class_test_1():
    p1 = Person(12, "Frank", 40, 90)
    # p2 = Person() does not have a default constructor any longer

    # self is passed implictly into the method
    p1.print_info()
    print (f"The ID is {p1.id_}")
    print(Person.COUNTER)
    p2 = Person(123, "John", 17)
    p3 = Person(96)
    print(Person.COUNTER)
    # you can also call an object's method using this way
    Person.print_info(p1)
    # this is how we call a class method, similar to normal static calls
    Person.class_method()

def class_test_2():
    c1 = Car("Porche", "911", 2023)
    c2 = Car.from_string("Ferrari-Alpha-2011")
    c3 = Car.static_method("BMW", "X5", 2024)

    print(c1)

def operator_test_1():
    op1 = OperatorLoading("abc", 12)
    op2 = OperatorLoading("def", 23)
    op3 = op1 + op2

    print("Done")
