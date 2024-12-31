## remove spaces from a string

## 1. replace all spaces with nothing
greeting = "Hello World! "
print(greeting.replace(" ", ""), ": 1")

## 2. remove all whitespace characters from a string (space, \t, \n)
version = "\tpy    310\n"
print(version.split(), ": 2")

## 3. instead of making a list, it can be joined with a nothing delimiter ""
print("".join(version.split()), ": 3")

## .4 can use regex
import re
print(re.sub(r"\s+", r"", version), ": 4") 
    #sub() looks like it replaces substrings
    # \s is all metacharacters which match whitespace characters
    # therefore its replacing all whitespaces with "" on the version variable

## what if its only EXTRA spaces we need to remove?
## 5. could use the split/join method from 3. but join with space
print(" ".join(version.split()), ": 5")

## what if only need to remove whitespace from beginning and end of a string?
## 6. use .strip
print(version.strip(), ": 6")
    # theres also lstrip() and rstrip()

## remove whitespace from ends of each line?
## 7. splitlines, strip each, then join
string = " Line 1\nLine 2  \n Line 3 \n"
stripped = "\n".join([line.strip() for line in string.splitlines()])
print(stripped, ": 7")

## 8. could use regex instead 
stripped = re.sub(r"^\s+|\s+$", r"", string, flags=re.MULTILINE)
print(stripped, ": 8")