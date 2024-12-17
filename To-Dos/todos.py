import sys

filename = sys.argv[1]

with open(filename) as file:
    lines = file.read().splitlines()
    ## all passed tests

for line in lines:
    if "TODO" in line:
        print(line)