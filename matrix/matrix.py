## was difficult to tackle this exercise due to the conversion of string to float in a list
## added difficulty was to create the list comprehensions and combo'ing them.

def matrix_from_string(string):     # "1 2\n10 20"
    string =string.rstrip("\n")
    
    splitted_by_new_line = string.split("\n")   #["1 2", "10 20"]

    split_by_space = [entry.split() for entry in splitted_by_new_line]  #[["1", "2"]["10", "20"]]

        ## solution by husband
    # split_by_space_dx = [[float(thing) for thing in entry.split()] for entry in splitted_by_new_line]
    # print(split_by_space_dx, 'dx')


    final_array = []

    for space_array in split_by_space:

        altered_space_array = [float(item) for item in space_array]
        # altered_space_array = []       # non-list comprehensive form
        # for item in space_array:
        #     item = float(item)
        #     altered_space_array.append(item)
        final_array.append(altered_space_array)

    return final_array

## all test cases pass, but not including the bonus!
    ## other solutions
    return [        # solution very similar to my husband's attempt
        [float(n) for n in row_string.split()]
        for row_string in matrix_string.splitlines()
    ]

    ## solution for bonus
    return [
        [float(n) for n in row_string.split()]
        for row_string in matrix_string.splitlines()
        if row_string.strip()   # added a condition if the resulting whitespace stripped is >0
    ]
