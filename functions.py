    ## functions are declared with def. you can input a default for parameters if none are given
    ## btw this only works in repl for some reason

def greet(name="world"):
    return print("Hello", name)

def product(numbers, start=1):
    total = start
    for n in numbers:
        total *= n
    return total

def to_kelvin(celsius):
    return celsius+273.15

    ## True and/or not False
    # these are boolean operators to link multiple conditions and alter boolean expressions 
def is_leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else: return False