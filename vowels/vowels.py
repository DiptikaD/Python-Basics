#   was solved by initially completing the append method + helper function. then translated the append method into a list comprehension.

def get_vowel_names(list):
    ## append method with helper function
    # vowel_names = []
    # for name in list:
    #     if process_vowels(name):
    #         vowel_names.append(name)
    # return vowel_names

    ## list comprehension method
    vowel_names = [name for name in list if process_vowels(name)]
    return vowel_names


def process_vowels(input_name):
    vowels = ["A", "E", "I", "O", "U"]

    for vowel in vowels:
        if vowel.casefold() in input_name[0].casefold():    # input_name[0] for first letter in name
            return True
        
# all tests pass

## other solutions
def get_vowel_names(names):
    return [
        name
        for name in names
        if name[0].upper() in "AEIOU"   # they iterated through a string instead of list, this bypasses the need for the helper function
    ]

# a little embarrassed i did not come up with that solution, but thats what next time is for!