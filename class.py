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
