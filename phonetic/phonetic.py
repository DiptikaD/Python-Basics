import sys

if len(sys.argv)==1:
    long = input("Text to spell out: ").upper()
else:
    words=sys.argv[1::]
    # print(words, "words")
    long = []
    for word in words:
        long += list(word)
        if word != words[-1]:
            long+= " "
        # print(word, words, "word", "words")
        # print(long, "long")
    
    # word = (let.upper() for let in sys.argv[1])

NATO = {"A":"Alfa", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", "F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"Xray","Y":"Yankee","Z":"Zulu", " ": ""}


for letter in long:
    # print(letter, "letter")
    for alph, abet in NATO.items():
        if letter.upper() == alph:
            print(abet)
        