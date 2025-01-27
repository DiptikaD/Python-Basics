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