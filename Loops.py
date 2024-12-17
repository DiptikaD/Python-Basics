
import random
    ## this is a simple and acceptable pythonic loop
favourite_fruits = ["blueberry", "raspberry", "lychee", "cherry", "orange"]

for fruit in favourite_fruits:
    print(fruit)

    ## this is looked down upon, indexing when not needed is discouraged, keep it simple. it is best practice to name appropriately too "fruit" is more descriptive than "i".
for i in range(len(favourite_fruits)):
    print(favourite_fruits[i])

    ## for loops in py are more like a foreach loop in java
    ## the "range(len())" can be replaced with "enumerate", hopefully see more of that

    ## here are different iterables
    ## LIST
moka_crimes = ["stinky", "smelly", "yells at everyone", "bites children", "throws up"]
    ## TUPLE
coordinates = (1,8,2)
    ## STRING
question = "What did moka do today? "
    ## SET
moka_cannot_eat = {"onions", "garlic", "spicy", "hair"}


print(question + random.choice(moka_crimes))
    ## TypeError: 'set' object is not subscriptable
# print("moka got told off for eating " + random.choice(moka_cannot_eat))
    ## but it can still iterate
for food in moka_cannot_eat:
    print("moka got in trouble for eating " + food)

    ## can also list to show all options in an iterable
print(list(moka_cannot_eat))
print(list(coordinates))

    ## Lists make it easy to append/add new entries, can add duplicates. remove with pop()
moka_crimes.append("steals socks")
print(moka_crimes)

    ## pop to remove, can store it at the same time. lists are ordered
removed_crime = moka_crimes.pop()
print(moka_crimes)

    ## lists have negative indexing, -1 = last value in list, -2 = second last
print(moka_crimes[-2])

    ## Lists are the most common data structure of python