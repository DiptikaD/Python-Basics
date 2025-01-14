"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return [number, number+1, number+2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    product = 0
    for card in hand:
        product += card
    return product/len(hand)

def approx_average_is_average(hand):
    first_last_avg = card_average([hand[0], hand[-1]])
    middle_avg = hand[len(hand)//2]
    avg=card_average(hand)
    return avg in (first_last_avg, middle_avg)

def average_even_is_average_odd(hand):
    even = hand[::2]
    odd = hand[1::2]
    if not even and not odd:
        return True
    if not even or not odd:
        return False
    
    return card_average(even) == card_average(odd)