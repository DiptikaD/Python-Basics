
import sys  ## reading from cli argument

filename = sys.argv[1]

with open(filename) as file:
    contents = file.read()  ## contents were read and stored into local variable

line_count = len(contents.splitlines())  ## specifically splits lines, it more effective than .split(\n) 
word_count = len(contents.split())  ## although we could .split(" "), it is more effective to leave out arguments as it will also consider newlined words.
print(f"Lines: {line_count}\nWords: {word_count}")

## this was a harder exercise, i must remember: with open(), then read. 