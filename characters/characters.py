    ## split the word and made it lowercase, if sort is true, 
    # then return the sorted version of the result, else just the result

def characters(word, sort=False):
    splitted = list(word.lower())
    if sort:
        return sorted(splitted)
    return splitted

    ## all tests pass including all bonus test cases


# other solutions

def characters(string, *, sort=False):  # * restricts users to only use keywords when calling the functions, 
    #it avoids someone putting in two parameters that are strings as opposed to putting in True
    """Return list of all characters in given string, lowercased."""
    if sort:
        return sorted(string.lower())   # removed one step from my solution
    return list(string.lower())
# ultimately comes down to which is more dev friendly to read