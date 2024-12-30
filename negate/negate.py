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