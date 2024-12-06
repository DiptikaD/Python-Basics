#if statements do not need brackets at all, its all just done by indentation
a = [1,2,3]
b = [1,2,3]
if a == b:
    print("they equal")

#there are also containment operators, "is this in that"
n = 2
print(n in a)
print(8 not in b) 
# is are used for identity of typing, this is not that
print(n is not None)

#multiple conditions in py, if, elif, else. this method seems better as a switch though
from random import randint

wavelength = randint(390, 780)
print(f"{wavelength}nm wavelength")

if wavelength < 390:
    print("Not visible")
elif wavelength < 455:
    print("Violet")
elif wavelength < 492:
    print("Blue")
elif wavelength < 577:
    print("Green")
elif wavelength < 597:
    print("Yellow")
elif wavelength < 622:
    print("Orange")
elif wavelength < 780:
    print("Red")
else:
    print("Not visible")