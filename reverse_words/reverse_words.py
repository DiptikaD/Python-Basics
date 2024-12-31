## basically i took the string of words, split them into separate words, reversed the order, joined them back into a string of words with spaces between

def reverse_words(words):
    rev = []
    splittered = words.split(" ")
    for word in reversed(splittered):
        rev.append(word)
    return " ".join(rev)



    ## other solutions
def reverse_words(sentence):    # without forloop
    """Return the given sentence with the words in reverse order."""
    words = sentence.split()    # split doesnt need parameters
    words.reverse()
    return " ".join(words)



def reverse_words(sentence):    # one liner
    """Return the given sentence with the words in reverse order."""
    return " ".join(sentence.split()[::-1])
#   return " ".join(reversed(sentence.split())) # whichever return seems nicer