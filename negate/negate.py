## solved! i understand the formatting of the list comprehension a bit better now. the inner for loop sits atop in its own [], then outside of that loop is the top layer of the logic
## therefore the anatomy is 
    # return [
    #   [inner for loop]
    #   outer for loop
    # ]

## i apprached the problem by writing out the full double forloops, then attempted to format the list comprehension by inserting information as needed.


def negate(list_of_lists):  #[[1, -2], [-3,4]]

    return [
        [-each_value for each_value in each_index]  # inner for
        for each_index in list_of_lists     # outer
    ]

    negated = []
    for each_index in list_of_lists:    # outer
        negative_values = []
        for each_value in each_index:       # inner
            negative_values.append(-each_value)
        negated.append(negative_values)
    return negated

# solved all tests!

## other solutions
    ## look identical to mine!!