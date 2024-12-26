scores= {"hup":"3400", "kwa": "5000", "oaa": "5020", "toa":"4025", "add": "100", "pig": "4020"}
    # this is a dictionary, it can show its value by presenting its key
print(scores["oaa"])
    # can update its value
scores["oaa"] = "5500"
print(scores["oaa"])
    # can add new entries in the same way to update
scores["slo"] = "3010"
print(scores)
    # can also check if a value exists in the dictionary
print("hup" in scores)
    # but doesnt work the same way for values
print("5000" in scores)

#   looping over dictionaries
    # generally dictionaries are meant for lookups and referencing. if looping is more important than lookup, then could instead benefit from using TUPLES
for keys in scores:
    print(keys)
    # generally keys are the most visible aspect of a dictionary, you can reference it, check for it, the value is protected by the key.
for name, points in scores.items():
    print(name, points)

#   removing a dictionary key
    # two methods, del statement, or pop function
del scores["kwa"]   # quietly deletes
slo = scores.pop("slo") # can save the value during deletion
print(scores,slo)

    # could attempt to delete a key that doesnt exist by dodging a keyerr
scores.pop("sti", "key not found")  # without the second statement, a keyerr would be given
scores.pop("hof", False)

#   implicit line continuation
    # where lines can be broken up without whitespace mattering when the code block is within ()[]{}
print("a"                 + 
              "b", 
              
              scores["pig"]) 
    # this is best done for formatting for readability, but could also just create a mess for no good reason
    # can also use \to wrap
import math, mailbox, \
        cmath, time # without the \ python will get upset
    # could also simple wrap the imports with ()
from collections.abc import (
    Hashable,Iterable, KeysView, Mapping,
        MutableMapping, Set)
    # functions and data structures already have their own brackets which you can format with