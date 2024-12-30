# to solve this, i had to write it out fully (without list comprehension) as there was an error, i then learnt that the item you wish to add must be stated first in the list comprehension for it to work (was not in lesson). 
# having struggles with str(letter).casefold() as it does not substitute what the .upper() or lower() conditional does to my surprise. 
    # turns out i can force the casefold() without parsing to str even though it does not pop up as a suggestion, however this might cause issues if a parameter passed is not a str!!!
# ultimately the list comprehension looks very wordy, and might be equal to the explicit form of appending to the new_list. 

def words_containing(input_list, letter):
    new_list = [something for something in input_list if letter.casefold() in something.casefold()]
    return new_list

    # new_list = []     ## appending version

    # for something in input_list:
    #     if str(letter).capitalize() in something or str(letter).lower() in something:
    #         new_list.append(something)
    # return new_list

## all test cases pass including bonus