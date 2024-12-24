#   solved base problem by simply creating new dictionary and adding new entries as the for loop iterates. value of original goes into the new dictionaries' key, vise versa
#   for the bonus, had to include the error_on_duplicates flag. this gives caution that if there are duplicate values as the dictionary is flipped, then it will raise an error. 
# the hardest part for me of this problem was to remember that python uses "and", not && or &.

def flip_dict(dictionary_input, error_on_duplicates=False):
    flipped={}
    for key, value in dictionary_input.items():
        if error_on_duplicates and value in flipped:
            raise ValueError
        flipped[value]=key
    return flipped

#   base problem and bonus problem tests all pass!

