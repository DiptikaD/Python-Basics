from collections import Counter

## unpacking can be done as long as items on both sides of the equation are equal
x,y = (4,5)
# x,y,z = (4,5) this is unbalanced and will throw an error
numbers = [1,2,3,4,5]
one, two, three, four, five = numbers
print(three)

## for values you do not care for, they can be denoted with _
_,_,three,_,_ = numbers
print(three, "_ assignments")

## can also slice
beginning, last = numbers[:-1], numbers[-1]
print(beginning, "beginning", last, "last")

## can also filter using asterisk
first, *rest = numbers
print(first, "first", rest, "rest")
first, *middle, end = numbers
print(middle, "middle with *")
    # using the * it allows for if there are multiple arguments that
    # could vary, preventing error

## there is also deep unpacking, where you can dig into data structures
colour, point = ("green", (1,2,3))
print(colour, point, "deep unpacking")
    # although it is assuming you know how many values is within those 
    # data structures

## can deep unpack an iterable
items = [4,2,5,6,2,4]
for i, (first, last) in enumerate(zip(items, reversed(items))):
    if first != last:
        raise ValueError(f"item {i} does not match: {first} != {last}")
    
# another example
def most_common(items):
    (value, times_seen), = Counter(items).most_common(1)
    return value
## in this example there is a , which plays a strong part in unpacking
# without the , it would result in an error
# the comma allows for the first output from Counter to be unpacked
# and that first index of that first output being:
    # value
    # times_seen

## can also pack multiple structures together in similar manner
fruits = ("apple", "banana", "cherry")
more_fruits = ["lemon", "kiwi", "melon", "blueberry"]
combined_fruits = *fruits, *more_fruits
print(combined_fruits, "combined tuple with list into tuple")

# could also instead combine into list
*combined_fruits, = *fruits, *more_fruits
print(combined_fruits, "combined both into list")
    # note the comma, which is necessary or else the *combined_fruits would error

