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