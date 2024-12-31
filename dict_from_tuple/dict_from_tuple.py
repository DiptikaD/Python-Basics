#   i didnt know how to approach this, so i began by showing what an example of the list_of_tuple could be. i then brute forced the answer by separating on each tuple, then indexing to get the key [0] and value [1::] from the tuple into the dictionary. 
#   once i partially solved brute forcing, i could identify how to optimise my solution to solve the problem

def dict_from_tuple(list_of_tuple):
    # list = [(1,2,3,4), (5,6,7,8)] example of input
    
    # tuple_1 = list_of_tuple[0]    brute force method
    # tuple_2 = list_of_tuple[1]
    # diction = {}
    # diction[tuple_1[0]]=tuple_1[1::]
    # diction[tuple_2[0]]=tuple_2[1::]
    # return diction

    diction = {}
    for tup in list_of_tuple:
        diction[tup[0]]=tup[1::]    # could potentially unpack and name the variables
    return diction



##  other solutions
def dict_from_tuple(tuples):
    """Turn list-of-tuples into a multi-valued dictionary."""
    return {    # returns the whole dictionary with minimal logic
        key: tuple(values)
        for key, *values in tuples
    }   # might be hard to replicate this in the future without more practice