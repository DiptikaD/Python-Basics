def len_or_none(input):
    try:    
        return len(input)
    except TypeError:   # error that pops up when an int is passed through
        return None     # exception for the int err
    
    # all tests pass
    # note that exceptions dont have to return error messages, they can just be for exceptions to a normal case