    ## tuples are immuteable, once created, it cannot be updated or added to. 
    ## here is a list of tuples. () is generally for tuples, [] for lists
menu = [("burger", 2.5), ("sausage", 2.0), ("sauce", 0.25)]
print(menu[1])    ## 'sausage', 2.0
print(type(menu))   ## class 'list'
print(type(menu[0]))    ## class 'tuple'

    ## there is a work around to get multiple return values by returning a tuple
def sum():
    v1 = int(input("value1: "))
    v2 = int(input("value2: "))
    total = v1+v2
    return v1, v2, total    ## multiple return values!

print(sum())