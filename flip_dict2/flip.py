def flip_dict_of_lists(dict_of_lists): 
    flipped = {}
    for key, values in dict_of_lists.items():
        for value in values:     # dict_of_lists={key:[value, value], key:[value]}
            flipped.setdefault(value, []).append(key)
    return flipped
## base solution
    # was difficult due to the very intricate wording of certain functions (.append).
    # did not succeed in bonuses

## other solutions
## BONUS 1
from collections import defaultdict

def flip_dict_of_lists(dict_of_lists, dict_type=None):
    """Return a "flipped" dictionary of lists."""
    flipped = defaultdict(list) # defaultdict creates mapping with default for all key lookups
    for old_key, old_values in dict_of_lists.items():
        for value in old_values:
            flipped[value].append(old_key)
    return flipped if dict_type is None else dict_type(flipped) # if dict_type was specified, parse it through and return

## BONUS 2
from collections import defaultdict

def flip_dict_of_lists(dict_of_lists, dict_type=None, key_func=None):
    """Return a "flipped" dictionary of lists."""
    if key_func is None:
        def key_func(key): return key   # if no key_func, a function was created that just returns the key
    flipped = defaultdict(list)
    for old_key, old_values in dict_of_lists.items():
        for value in old_values:
            flipped[key_func(value)].append(old_key)    # if key func, then parse the new_key through and append
    return flipped if dict_type is None else dict_type(flipped)