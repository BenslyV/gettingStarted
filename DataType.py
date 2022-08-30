
#getting the data type
import random

name='bensly'
print("type of the name is")
print(type(name))

#Setting the Specific Data Type
x = float(20.5)
print(type(x))


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random number generator
print(random.randrange(1,100))

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes:

#Example
#You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

name = "Varma"

print(type(name))

print("hello"[0])

# adding two digits
num ="28"
print(int(num[0])+int(num[1]))

#BMI calculator

age = 30
weight = 78
height = 1.67
bmi = weight/(height*2)
print(type(bmi))
print(int(bmi))

# fstrings in Python

age = 10
name = "John"

print(f"My name is {name} and my age is  {age}")

# no of weeks left calcuator

age = input("what is your age")

age_in_weeks = age * 52

age_90 = 90*52
print(f"no of weeks left {age_90} - {age_in_weeks}")


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


# 1.exercise
print("Exercise Printing")
word = ['1','2','3','4']
word[ : ] = [ ]
print(word)

#2.erercise

L = ['one','two','three', 'four', 'five', 'six']
print(sorted(L))
print (L)

# 3. exercise
#
# import ast,sys
# input_list = (sys.stdin.read()).split(',')
# # Write code to remove 'SPSS'
# # input_list.remove("SPSS")
# # Write code to append 'SPARK'
# input_list.append("SPARK")
# print(input_list)

# 4. erercise

print(" exercise 4 printing")
import ast,sys
input_str = sys.stdin.read()
inp =input_str.split("_")
print(type(inp))
first_name = inp[1]
second_name = inp[0]
customer_code = inp[2]
print(first_name)
print(second_name)
print(customer_code)

