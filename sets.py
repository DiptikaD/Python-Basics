    ### sets are mutable and unordered collection of hashable objects!
    ## dups are not allowed, but they can hold mutliple different data types, even nested structures such as tuple of tuples. 
    ## frozensets are an immutable version

    ## sets are defined using the same brackets as dictionaries, but with one element.
littleSet = {"small", "tiny", "microscopic", "too little", "small", "small"}
print(littleSet)
    ## duplicates are silently ommited 

    ### can: 
    # - iterate (for item in <set>)
    # - in and not in checks
    # - len()
    # - copy()

    ### cannot:
    # - index!
    # - order/sort/insert
    # - slice!
    # - concatenate with + 

bigSet = {"large", "huge", "small", "colossal"}
    ## can check if there is not any overlap in elements
print(bigSet.isdisjoint(littleSet), "is disjointed")
    ## false means there is shared elements, true means there isnt

## subsets and supersets
    # checks if all elements are present in another set
print(littleSet <= bigSet, "false, subset operator")
    # false

smallSet = {"small", "microscopic"}
print(smallSet <= littleSet, "subset operator")
    # true, is false the other way around!

print(smallSet.issubset(littleSet), "is subset")
    # true

## opposite can be tested with superset
print(littleSet.issuperset(smallSet), "superset")
    # true