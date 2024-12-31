# when running a function, if the program does not run as intended due to a unique but possible exception, note down the error that pops up in the traceback
# this error can be used to either try code to catch the exception, or to find what causes the exception and raise it

## TRY/CATCH exceptions
# SEE length or none

## RAISE an exception
    # here is a function for checking if a number is prime


from math import sqrt

# def is_prime(number):
#     for candidate in range(2, int(sqrt(number))+1):
#         if number % candidate == 0:
#             return False
#     return True

## passing a negative int will raise/throw a valueErr exception from the traceback
## a floating number doesnt raise an exception, but it falsely flags it as a prime when it isnt.
## passing 0 or 1 returns a true prime which isnt mathmatically correct, this too is an exception

def is_prime(number):
    if isinstance(number, float):
        raise TypeError(f"Only integers are accepted: {number}")
    if number < 2:
        raise ValueError(f"Only integers above 1 are accepted: {number}")
    for candidate in range(2, int(sqrt(number))+1):
        if number % candidate == 0:
            return False
    return True