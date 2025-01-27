##  Classes, like in Java have many names, object, instance, product, but they are all encompassing a class
    ## to call an attribute of a class, you call it without using brackets

class Product:
    def __init__(self, name, cost, price):  # definining attributes
        self.name = name
        self.cost = cost
        self.price = price

    def profit_margin(self):    # class methods
        return self.price - self.cost
    
## can call it by referring to it as such:
duck = Product(name="rubber duck", cost =1, price=5)
print(duck.name, duck.profit_margin())

# note that we will have to import the class if calling from a different .py

## note that type and classes are the same, therefore:
    #- list, dict, tuple, int, str, set and bool
    # are all classes!

## what are the 'self' parameters in the instance variables and methods?
    # they are automatically filled to be references to the object itself
    # they MUST be stated as the first parameter
    # they can be called other names, but programatically it is looking for 'self'
    # think of them as 'this' in java
    # without the self, the class cannot find the instantiated object that was called

## the __init__ pronounced as dunder init is the important initialiser method
    # without it the class would not know how to assign itself when called
    # is the first and most important method of a class

# -------------------------------------- #

## inheriting from another class!
from collections import Counter

class FancyCounter(Counter):    ## Inheriting by calling the class immediately
        # can inherit from multiple classes! but not common
        # no __init__ needed as it is present in Counter which is called

    def __setitem__(self, key, value):  # to set a limit to common occurance being no less than 0
        value = max(0,value)
        return super().__setitem__(key, value)
        ## this works by referring the parent/super class and overwriting their __setitem__ as this

    def commonest(self):
        (value1,count1), (value2, count2) = self.most_common(2)     # .most_common from parent class
        if count1 == count2:
            raise ValueError("No unique most common Value")
        return value1
    
## calling our new class and method:
letters = FancyCounter("Hello there!")
print(letters)  # prints all nice due to the __repr__ method in Counter for string representation

print(letters.commonest(), "<--- commonest output")

letters['l'] = -2   # reassigning occurance
print(letters)  # it has no logic for negative commonality, so we will make a new method for it in our new class
    # created the __setitem__ method which has fixed this.

# -------------------------------------- #

# singletons!
# where a class only allows the creation of one instance of itself
    # for example, None is a singleton
new_none = type(None)()
print(new_none is None, "new_none is None")
    # although we clearly created a new instance of none, it is still the exact same

# to create a singleton, just need to add the __new__ method to a class:
class EventTracker:
    _self = None    # for a singleton's sake, this is required

    # what is cls? 
        # it is like self but at a class level, it is refering to THIS class.

    def __new__(cls):   # this method is a constructor method
        if cls._self is None:   # if hasnt been initialised before, then it creates the instance, otherwise returns the existing one
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):     # is initiated after to prevent a new instance
        self.api_url= "http://example.com"
    
    def track(self):
        print(f"TODO track event at {self.api_url}")

tracker = EventTracker()
tracker2 = EventTracker()
print(tracker is tracker2, "tracker is tracker2")


## Creating a Singleton with global object instead