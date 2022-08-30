from sys import modules

tuple1 = ("a", "b", "c", "d", "e")
mytuple = ("Bensly",)
thisisnottuple = ("CommaMissing")
print(tuple1, thisisnottuple)
print(len(tuple1))

# A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)

# access tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Check if Item Exists

if "apple" in mytuple:
    print("Apple Present in mytuple")

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list,
# change the list, and convert the list back into a tuple.

y = list(thistuple)
y[1] = "Grapes"
print(y)
y.extend("mango")
print(y)
thistuple = tuple(y)
print("Printing tuple after extending")
print(thistuple)
print(type(thistuple))

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# packing a tuple

fruits = ("apple", "banana", "cherry")
# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Example
# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
print(type(red))
print(type(green))

# Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Python - Loop Tuples

print("Python - Loop Tuples")
for a in fruits:
    print(a)

# Use the range() and len() functions to create a suitable iterable.
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
for i in range(len(thistuple)):
    print(thistuple[i])

# Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
print("My Tuple count")
print(fruits.count("apple"))

# help (“modules”)

print("Printing today Aug 19")
print(mytuple[0])