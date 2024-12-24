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

#   JOINING
    #universally (for all datastructures + files + numbers) can join together using .join()
joined = " ".join(colours)
print(joined)
    ## the " " is a delimiter, it will be inserted between each entry, it can be anything, it can also be nothing
joined2 = " ugh! ".join(colours)
print(joined2)
file=open("my_file.txt")
filejoin = ", ".join(line.rstrip("\n") for line in file)    ## this removes the \n and replaces with , 
print(filejoin)

    ## with numbers it must be converted to str
numbers = [3,4,4,3,5,5,66,7,7]
print(" $".join(str(n) for n in numbers))
    ## can do an inline for loop to convert to str and join.