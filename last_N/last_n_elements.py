    ## my dodgy solution

def last_n_elements(list, n, reverse=False):
    start = 0
    end = 0     ## golf = "golfing"
    step = 1
    if reverse is True: 
        start = -1
        step= -1    ##golf[-1:-2:-1]
        end= -n -1
    elif n == 0:
        return list[:n:step]
    else: 
        start=-n
        end= 400  ##golf[-2:0:1]
    
    return list[start:end:step]

## had some trouble because i named the function parameter/argument as rev, rather than reverse, this caused the tests not to identify the variable

    ## solution from tutor. although this solution is much more succint, it is harder for me to follow, though that may be as the complex indexing is a new concept!

def last_n_elements(sequence, n, reverse=False):
    """Return last n items from given list."""
    if n <= 0:
        return []   ## they hardcoded the 0
    if reverse:
        return sequence[-n:][::-1]  ## they did the normal index, then reversed by adding on the [::-1]
##      return sequence[:-n-1:-1]   ## instead to separating the reverse slice above
    else:
        return sequence[-n:]