import sys

if len(sys.argv)==1:
    long = input("Text to spell out: ").upper()
else:
    words=sys.argv[1::]
    long = []
    for word in words:
        long += list(word)
        if word != words[-1]:
            long+= " "

NATO = {"A":"Alfa", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", "F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"Xray","Y":"Yankee","Z":"Zulu", " ": ""}


for letter in long:
    # print(letter, "letter")
    for alph, abet in NATO.items():
        if letter.upper() == alph:
            print(abet)
        

## i only managed to solve the base problem + 1 bonus
## i had great difficulty splitting the text file into two indexes for easy referencing as a new dictionary


## here are other solutions

from argparse import ArgumentParser
from pathlib import Path
import unicodedata  # for bonus #3


alphabet = {
    'a': "Alfa",
    'b': "Bravo",
    'c': "Charlie",
    'd': "Delta",
    'e': "Echo",
    'f': "Foxtrot",
    'g': "Golf",
    'h': "Hotel",
    'i': "India",
    'j': "Juliett",
    'k': "Kilo",
    'l': "Lima",
    'm': "Mike",
    'n': "November",
    'o': "Oscar",
    'p': "Papa",
    'q': "Quebec",
    'r': "Romeo",
    's': "Sierra",
    't': "Tango",
    'u': "Uniform",
    'v': "Victor",
    'w': "Whiskey",
    'x': "X-ray",
    'y': "Yankee",
    'z': "Zulu",
}


parser = ArgumentParser()   # parser was used to identify if -f and file was present
parser.add_argument('words', nargs='*')
parser.add_argument('-f', '--filename')
args = parser.parse_args()


if args.filename:
    lines = Path(args.filename).read_text().splitlines()    # reads without opening/closing, splits
    for line in lines:
        letter, word = line.split()     # unpacks into letter and word, i needed this
        alphabet[letter.lower()] = word # rewrites the nato alphabet with the file's alphabet


words = " ".join(args.words)    # to add \n between multiple words
if not words:
    words = input("Text to spell out: ")
for char in unicodedata.normalize("NFKD", words.lower()):   # from the unicode database, it turns the fancy unicode back to normal
    if char in alphabet:
        print(alphabet[char])
    elif char == ' ':
        print()

# very difficult exercise! but I managed to get the base + one bonus!