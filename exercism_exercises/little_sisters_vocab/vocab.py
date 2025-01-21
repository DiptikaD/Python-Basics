"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    return f"un{word}"


def make_word_groups(vocab_words):
    return " :: ".join([vocab_words[0]] + [vocab_words[0] + word for word in vocab_words[1:]])


def remove_suffix_ness(word):
    if "iness" in word:
        return f"{word[:-5]}y"
    return f"{word[:-4]}" 



def adjective_to_verb(sentence, index):
    sentence2=sentence.replace(".","")
    words = sentence2.split()
    return f"{words[index]}en"

## all tests pass