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
        input_grade = input_grade+0.5

    round_grade = math.floor(input_grade)

    for grade, score_range in a.items():
        if round_grade>=score_range[0] and round_grade<=score_range[1]:
            print(grade, input_grade, round_grade)
            return grade

      
def calculate_gpa(list_of_scores):
    points = {"A+":4.33, "A":4.00, "A-":3.67, "B+":3.33, "B":3.00, "B-":2.67, "C+":2.33, "C":2.00, "C-":1.67, "D+":1.33, "D":1.00, "D-":0.67, "F":0.00}
    sum = 0

    for score in list_of_scores:
        for key, value in points.items():
            if score == key:
                sum += value
    return sum / len(list_of_scores)