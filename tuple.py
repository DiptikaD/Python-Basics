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

    ## tuple unpacking / multiple assignment / iterable packing
    ## are all terms for reassigning tuple values into variables
value1, value2, total = sum()   ## <<------ unpacking!
print(value1)
print(value2)
print(total)
    ## what happened is although a tuple was created, you can take those values and use them separately as values. 
three = 3,2,1
x,y,z = three
print(x+y-z)    ## you can use them as normal variables without having to index the tuple anymore

    ## dictionary is best unpacked via for loop
things = {"chicken":2, "feed":50, "coop":1} ## <<--- this is a dictionary; key/value
for stuff in things.items():    ## things.items() lists all key/values
    thing, count = stuff    ## unpacking // chicken 2; feed 50; coop 1
    print(thing,count)


def parse_time(time_string):
    """Return total seconds from MM:SS timestamp."""
    minutes, seconds = time_string.split(":")      ## <<---- unpacking with a split!
    return int(minutes)*60 + int(seconds)

    ## whenever an indexing is used, it could be possible to unpack instead

    ## SLICING!!
    ## an inbuilt data structure function that allows you to create a new data structure from what was given
greet = "hello why are you here?"
print(greet[0:5])
print(greet[-5:])
    ## [start:end], where start is inclusive, but end is exclusive
weird_greet = greet[::2]    ## <<-- step function!
print(weird_greet)
reverse_greet = greet[::-1]
print(reverse_greet)
    ## the step function means it will skip over the number given
    ## [::2] skips over the second index
    ## [::-1] goes in reverse! though there are other functions to reverse
    ## NOTE: slicing can be done on anything that can be indexed, this includes tuples, lists, dictionaries and strings
print(greet[:200]) ##<<----- there is no out of bounds err!
print(greet[-3:])