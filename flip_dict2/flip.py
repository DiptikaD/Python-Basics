def flip_dict_of_lists(dict_of_lists): 
    flipped = {}
    for key, values in dict_of_lists.items():
        for value in values:     # dict_of_lists={key:[value, value], key:[value]}
            flipped.setdefault(value, []).append(key)
    return flipped
## base solution
    # was difficult due to the very intricate wording of certain functions (.append).
    # did not succeed in bonuses
