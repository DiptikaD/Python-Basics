def split_in_half(sequence):
    half = len(sequence)//2
    first_half = sequence[0:half]
    second_half = sequence[half:]
    return first_half, second_half

## all tests passed including bonus!