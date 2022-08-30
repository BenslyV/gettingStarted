myFirstList = ["apple", "orange", "mango", "dragonfruit"]
languagesKnown = ["java", "c", "C++", "python"]
print(myFirstList)
print(languagesKnown)

thisList = ["apple", "banana", "cherry", "apple", "cherry"]
print(thisList)
print(len(myFirstList))

# A list can contain different data types
list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thisList1 = list(("a", "b", "c"))
print(thisList1)

print(list1[0])
print(list1[1])
print(list1[-1])
print(list1[0:2])

if "apple" in mylist:
    print("Yes, we have apple in the list")

# Change Item Value
thisList1[2] = "mn"
print(thisList1)

thisList1.insert(2, "fg")
print(thisList1)
# add List item
thisList1.append("z")

print(thisList1)

# extend list

abc = ["a", "b", "c"]
thisList1.extend(abc)

print(thisList1)

# Remove Items
thisList1.remove("mn")
print(thisList1)
thisList1.pop()
print(thisList1)

thisList1.clear()
print(thisList1)

thisList1.extend(thisList)

print(thisList1)

for a in thisList1:
    print(a)

# looping using while loop
print("looping using while loop")
thisList2 = ["1", "2", "3", "4"]
i = 0
while i < len(thisList2):
    print(thisList2[i])
    i = i + 1
# loop comprehensive
[print(x) for x in thisList2]

print("looping using for loop")
for b in thisList2:
    newlist1 = []
    print(b)
    if "3" in b:
        newlist1.append(b)
        print(newlist1)

print("Printing using comprehensive loops")
skills = ["Data Science", "Devops", "Testing", "Management"]
newskills = [x for x in skills if "Devops" in x]
print(newskills)

newskills2 = []
newskills2 = [x for x in skills if x != "Testing"]
print("Printing newskills2")
print(newskills2)

print(range(50))

newlist3 = []
newlist3 = [x for x in range(50) if x != 45]
print(newlist3)

# sort lists

skills.sort()
print(skills)
skills.reverse()
print(skills)

words = ["john", 'Kumar', "BALU", 'Praveen', "Mani"]
numbers = [70, 30, 15, 4, 105]
words.sort(key=str.lower)
print(words)
print(numbers)

# copy a list

words2 = words.copy()
print("Copying list")
print(words2)

# join lists
words3 = words + words2
print(words3)

'''words4 = words.extend(words3)
print(words4)

for x in words4:
    words.append(words4)
print("words")'''

print("Printing today Aug 19")
print(myFirstList[0])