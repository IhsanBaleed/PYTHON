from basics.DT import array_test_1, switch_test
from basics.Inheritance import *
from basics.Classes import *
from DesignPatterns.ProtoType import *
from DesignPatterns.StateMachine import test_sm


def main():
    test_sm()


# when a script is running directly, __name__ has a value of main
# when imported as a module, __name__ has the value of the module.
if __name__ == "__main__":
    main() # kicks off main

