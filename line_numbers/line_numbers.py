import sys

file = sys.argv[1]
with open(file) as ofile:
    for n, line in enumerate(ofile, start=1):
        print(n, line.rstrip("\n"))