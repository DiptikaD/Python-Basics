# Problem Statement
# I'd like you to write a program called unsmart.py which accepts a file as an argument and prints out the contents of the file with smart quotes converted to "dumb" quotes. Smart quotes are the angled quotes and apostrophes, namely ‘, ’, “, and ”.

# In many word processors (MS Word, Google Drive, etc.) typing in the ' character on a US-style keyboard will result in the word processor entering either ‘ or ’ and typing in " will result in either “, or ”.

# basically replace “ with ", ect

#provided code:

from argparse import ArgumentParser, FileType

parser = ArgumentParser()
parser.add_argument("file", type=FileType(encoding="utf-8"))
args = parser.parse_args()

text = args.file.read()

# TODO unsmartify the text somehow

print(text
      .replace('“', '"')
      .replace('”', '"')
      .replace('‘', '\'')
      .replace('’', '\'')
      .rstrip("\n")
      )

#you can line up functions on the same variable to get a big chunk done
# pass all tests