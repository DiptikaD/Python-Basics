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

