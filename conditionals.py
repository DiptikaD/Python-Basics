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

# below we see a python's ternary. "this if thing, else that". 
# NOTE: The ternary also automatically flags 0 = false, 1 = true
# therfore its really: this if true, else that 
coin_flip = randint(0, 1)

print("Heads" if coin_flip else "Tails")

#for the sake of random, the choice method can spin between the provided options:
import random

print(random.choice(("Coconut", "Lime", "Sour cream")))
#could potentially put a tuple in place

#substrings can be compared to check if something appears in a another string
banana = "banana"
bananaSentence = "I don't want to eat banana"
print(banana in bananaSentence)
#case insentitive would be:
wantWord = "Want"
print(wantWord.casefold() in bananaSentence.casefold())