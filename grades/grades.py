    # i approached this by creating a dictionary of the key/value pairs for the scores, i decided on this as I will be constantly looking up the k/v to match the grades/scores. I could have created an equation to convert the grade based on the score, however, the added flags for the bonus section would get messier. this is more legible to me
    # the suffix bonus calls for a "keyword-only" argument, this is remedied by the *, without it the test will fail everytime! 
    # to separate the option if suffix or not, I created an empty dictionary which would be referenced in the meat of the logic (returning the grade). This allows for which set of rules is used, if the result is simply D, or if it could be D-,D,D+. I could pass only the suffic_dict and write logic to calculate the base grade, but i am not too sure on the math, therefore went instead with mutliple grading dictionaries (grade_dict & suffix_dict).
    # round bonus was tricky as the test CALLS for round overwriting the built in python function which would round the score in the first place. This is most unfortunate, but an easy work around.
    # despite if round=T or not, the score will still be floored, this was necessary for my base solution and has been consistent through test cases.
    # final bonus was a simple additional function to average a list of given scores. i created another dictionary of the weighting of the scores, then have them constantly referenced against the list of scores provided. add up the values and return the averaged score.

import math

def percent_to_grade(input_grade,*, round=False, suffix=False): # keyword only *
    grade_dict = {"F":(0,59), "D":(60,69), "C":(70,79), "B":(80,89), "A":(90,100)}
    suffix_dict = {"F":(0,59), "D-":(60,62), "D":(63,66), "D+":(67,69), "C-":(70,72), "C":(73,76), "C+":(77,79), "B-":(80,82), "B":(83,86), "B+":(87,89), "A-":(90,92), "A":(93,96), "A+": (97,100)}
    a = {}

    if suffix:
        a = suffix_dict
    else:
        a = grade_dict

    if round:
        input_grade = input_grade+0.5   # round up

    round_grade = math.floor(input_grade)

    for grade, score_range in a.items():
        if round_grade>=score_range[0] and round_grade<=score_range[1]: # score_range[0] being the min, [1] being the max. couldnt figure out how to unpack multiple values in a key
            # print(grade, input_grade, round_grade)    #troubleshooting printer
            return grade

      
def calculate_gpa(list_of_scores):
    points = {"A+":4.33, "A":4.00, "A-":3.67, "B+":3.33, "B":3.00, "B-":2.67, "C+":2.33, "C":2.00, "C-":1.67, "D+":1.33, "D":1.00, "D-":0.67, "F":0.00}
    sum = 0

    for score in list_of_scores:
        for key, value in points.items():
            if score == key:
                sum += value
    return sum / len(list_of_scores)

    ## base test passes including all four bonus test cases!!

## other solutions!

## ROUND BONUS
builtin_round = round       # gave round() an alias before function existed

GRADES = [      # reversed the order of his dictionary to mine
    (97, 'A+'),
    (93, 'A'),
    (90, 'A-'),
    (87, 'B+'),
    (83, 'B'),
    (80, 'B-'),
    (77, 'C+'),
    (73, 'C'),
    (70, 'C-'),
    (67, 'D+'),
    (63, 'D'),
    (60, 'D-'),
]

def percent_to_grade(percent, *, suffix=False, round=False):
    if round:
        percent = builtin_round(percent)    # the built in round works now, but it ISNT the correct method for only wanting to round up by half. instead can insert my percent += percent+0.5. He made it as another function he called upon.
    for min_percent, letter in GRADES:
        if min_percent <= percent:
            return letter if suffix else letter.rstrip('-+')    # if suffix is false, then it will always fall under the correct lettering and the -/+ will be stripped, else, it will specify the respective suffixed grade!
    return 'F' # else all minimums, then receive F

### GPA BONUS

GPAS = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'F': 0,
}


SIGNS = {
    '-': -0.33,
    '+': +0.33,
}


def calculate_gpa(grades):
    points = sum(GPAS[g[0]] for g in grades)    # checks each letter and sums up
    points += sum(SIGNS.get(g[-1], 0) for g in grades)  # checks each sign and sums up
    return points / len(grades) 
# this solution is very crafty, but harder for me to follow initially as there is alot going on.