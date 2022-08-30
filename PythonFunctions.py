# Creating my first Python function
print("Before my function execution")


def my_function():
    print("Printing my first Python function")


my_function()

# Passing arguments


def my_function1(name):
    print(name + " " + " is my name")


my_function1("Bensly")


def my_fun2(name, age):
    print("My name and age is " + name + "  " + age)


my_fun2("Bensly", "30")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "lname")


def function3(*kids):
    print("Kids names are" + kids[1])


function3("Jon", "Jona", "Jelsi")


# Keyword Arguments

def learn4(skills, jobs, sal):
    print("Printing"+skills+" "+jobs+""+sal)


learn4(jobs="Data Scientist", skills="Python", sal="20L")

# Default Parameter Value


def coll(govt="GCT"):
    print(govt)


coll("SXCCE")
coll()

# To let a function return a value, use the return statement:


def return_function(val1, val2):
    val3 = val1 + val2
    return val3


return_Val = return_function(5, 6)
print(return_Val)

# function definitions cannot be empty, but if you for some reason have a
# function definition with no content, put in the pass statement to avoid getting an error.

def fun1():
    pass
