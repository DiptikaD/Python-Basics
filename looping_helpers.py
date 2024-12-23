#   REVERSING
colours = ["purple", "blue", "green", "pink", "red"]
# there are multiple ways to reverse, a majority of data structures can be reversed with the:
colours[::-1]
# can input that into a for loop and reverse in that manner
for colour in colours[::-1]:
    print("weird", colour)

# lists have .reverse(), but thats only in LIST data structure. it also modifies the original
# an acceptable way is looping revered
for colour in reversed(colours):
    print("dark", colour)

# can also manually/lazily iterate through via next()
iterateRev = reversed(colours)
print(next(iterateRev), next(iterateRev), next(iterateRev))
    ## "don't store their results anywhere. Instead, these functions return objects that are meant to be looped over immediately".
