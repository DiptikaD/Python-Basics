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


#   default dictionary values
        ## to look up a key that is not in the dictionary and set it a default value.
        # get method looks up a value without raising an exception for missing keys
print(scores.get("zop", 0), "zop score") # it checked and did not add the key, so it returned the default
print(scores.get("hup", 0), "hup score")
    # if no default value is provided, then it defaults to None. 
#   what about setting a default value
        # can use setdefault
from dataclasses import dataclass

@dataclass
class Item:     # looks like this is a class defined as Item with two attributes
    name: str
    color: str

items = [
    Item("duck", "purple"),
    Item("water bottle", "purple"),
    Item("uni-duck", "pink"),
    Item("sticky notes", "yellow"),
]
items_by_color = {}
for item in items:
    items_by_color.setdefault(item.color, [])   # the class allows the key/values to be separated by .color and .name
    items_by_color[item.color].append(item.name)
#   items_by_color.setdefault(item.color, []).append(item.name) # instead of doing the two upper lines, can combine

print(items_by_color)