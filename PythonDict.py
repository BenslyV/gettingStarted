myfirstDict = {"Name": "Bensly",
               "Age": "30",
               "Gender": "Male",
               "Skills": ["Python", "Data", "Java"]}
print(myfirstDict)
print(type(myfirstDict))
print(len(myfirstDict))
print(myfirstDict["Name"])

# Accessing Items

print(myfirstDict["Age"])
x = myfirstDict.get("Gender")
print(x)

y = myfirstDict.keys()
print(y)
myfirstDict["Job"] = "UST"
y1 = myfirstDict.keys()
print("After adding the new keys")
print(y1)

print(myfirstDict.values())
print(myfirstDict.items())

# Check if Key Exists

if "Age" in myfirstDict:
    print(" Yes. Age is present")
else:
    print(" No.Age is not present")

# Change Values

print("Script for changing values")
myfirstDict.update({"Job": "CTS"})
myfirstDict["Age"] = 31
print(myfirstDict)

# add items

myfirstDict["location"] = "Nager Coil"
print(myfirstDict)

# myfirstDict.pop()

# Loop Through a Dictionary

print("Dic Loops")
for x in myfirstDict:
    print(myfirstDict[x])

print("looping items")
for y in myfirstDict.items():
    print(y)

# Copy a Dictionary
print("Copying a Dic")

mydic2 = myfirstDict.copy()
print(mydic2)

mydict = dict(mydic2)
print(mydict)

# Nested Dic

myfamily = {
    "child1": {
        "Name": "Rohan",
        "Age": 10
    },
    "child2": {
        "Name": "Rohit",
        "Age": 15
    }
}

print(myfamily.values())
print(myfamily.keys())
print((myfamily.items()))


