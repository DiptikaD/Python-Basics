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

bigSet = {"large", "huge", "colossal"}
    ## can check if there is not any overlap in elements
print(bigSet.isdisjoint(littleSet))
    ## false means there is shared elements, true means there isnt

