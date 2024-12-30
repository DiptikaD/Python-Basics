    ## what are list comprehensions?
    ## looks like theyre a compact way to do a for loop and conditionals
screencasts = [     #our list
    "Data structures contain pointers",
    "What is self?",
    "What is a class?",
    "Slicing",
    "How to make a function",
    "Methods are just functions attached to classes",
]
names = []      # a new list which is is just screencasts with Every First Letter Capitalised
for name in screencasts:
    names.append(name.title())
    print(names)

names = [name.title() for name in screencasts]      # this is the list comprehensive equivalent of the above code
    # normal for loops allow for looping over an iterable and perform ANY actiom. but list comprehensions are SPECIFICALLY for looping over some existing iterable and making a new list out of it, usually while changing each element a little bit along the way. can also use list comprehensions for filtering elements down, only including items which match.

    ## filtering with comprehensions
short_names = []
for name in screencasts:
    if len(name) <= 30: # if length is <=30, then append to short_names
        short_names.append(name.title())
        print(short_names)

short_names = [name.title() for name in screencasts if len(name) <= 30]
#   (1)          (2)        (3)                     (4)

    ## the anatomy of a list comprehension is: 
        # (1): name of new list to append to
        # (2): item to add to list
        # (3): looping logic
        # (4): conditions if any

    ## the general rule to convert for loops into list comprehensions:
        # if you have an empty list to append to
        # iterating through
        # one end to an unlimited if statement
            # if there is an else, then then it can be condensed down by using a helper function!!
            # for example:
shortened = []
for name in screencasts:
    if len(name) > 30: # this complex if/else could be eliminated with a helper function

        shortened.append(name[:30-3] + "...")
    else:
        shortened.append(name)  

def ellipsify(name):
    if len(name) > 30:
        return name[:30-3] + "..."
    else:
        return name
 
shortened = [] 
for name in screencasts:    # altered for loop from above function
    shortened.append(ellipsify(name))

shortened = [   # list comprehension from above loop!
    ellipsify(name)
    for name in screencasts
]


## nested list comprehensions
## for when making a list of lists
def strings_to_numbers(matrix): # taking this and turning it into a nested list comprehension
    new_matrix = []     # second comprehension
    for row in matrix:
        new_row = []    # first comprehension
        for n in row:
            new_row.append(int(n))
        new_matrix.append(new_row)
    return new_matrix

    # here is the function altered for the first comprehension
def strings_to_numbers(matrix):
    new_matrix = []
    for row in matrix:
        new_matrix.append([int(n) for n in row])
    return new_matrix

    # here is the second
def strings_to_numbers(matrix):
    new_matrix = [
        [int(n) for n in row]
        for row in matrix
    ]
    return new_matrix   # return is useless as we could one line everything

    ## final form
def strings_to_numbers(matrix):
    return [
        [int(n) for n in row]
        for row in matrix
    ]