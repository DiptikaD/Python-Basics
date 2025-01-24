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
