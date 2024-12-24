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