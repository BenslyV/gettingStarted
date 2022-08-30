print("Hello world this is my first program")
print("Hello  exit before command")
#block
if 5 > 2:
    print("Five is greater than two!")

if 6 > 2:
    print("Six is greater than two!")
    print("Six is greater than two!!!!!!!!!!!!!!!!!")

#Python Variable
x = 5

y = "Hello, World!"

print(x, y)

#exit command
#exit()
print("Hello after exit command")

#learning command


#This is a comment
print("Hello, World! Commond")
print("Hello, World!") #This is a comment

#This is a comment
#written in
#more than just one line
print("Hello, World!")
"""
This is a comment
written in
more than just one line
"""

x = 5
y = "John"
print(x)
print(y)

print(type(y))
print(type(x))

x1 = "John is my name x1"
# is the same as
x2 = 'John is my name in x2'
print(x1, x2)

#variable name
a=1
b1=2
_b='test'
a_="Test2"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x1, y1, z1 = 'Orange1', 'Banana1', 'Cherry1'
print(x1)
print(y1)
print(z1)

"""One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:

Example"""
x = y = z1 = "Orange"
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print( x + y + z )

x = "awesome and X is a global variable"


def myfunc():
    global x3
    x3="awesome and X3 is a local variable"
    print("Python  function is " + x3)


#x3 = "awesome and X3 is a global variable here"
myfunc()

print("Trying to print local variable"+x3)





