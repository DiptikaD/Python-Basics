import math

def dog_and_bun_packs_needed(guests):
    buns = 8
    hot_dogs = 10
    buns_needed = math.ceil(guests/buns)
    hotdogs_needed = math.ceil(guests/hot_dogs) ## round up on guest to dog ratio for packs

    return buns_needed, hotdogs_needed  ## two return statements from tuples

    ## tests all passed