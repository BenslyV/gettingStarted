firstPythonSet = {"item1", "item2", "item3", "item4", "item5"}
print(type(firstPythonSet))
print(firstPythonSet)
print(len(firstPythonSet))

# print(firstPythonSet[0])

thisset = {"apple", "banana", "cherry", "apple", "cherry"}

print(thisset)

# Example
# String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

# Access Items
for x in firstPythonSet:
    print(x)
    if "item1" in firstPythonSet:
        print("Yes. Item1 is there")
    else:
        print("Item1 is not there")

print("apple" in set1)

# Python - Add Set Items

set1.add("mango")

print(set1)

set1.update(set2)
print(set1)

# Python - Remove Set Items

set1.remove(9)
print(set1)
# set1.remove(42)
set1.discard(42)
set1.pop()

# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Join Two Sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
set4 = set3.update(set2)

print(set3)
print(set4)

# The intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)




