"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    return f"un{word}"


def make_word_groups(vocab_words):
    return " :: ".join([vocab_words[0]] + [vocab_words[0] + word for word in vocab_words[1:]])

