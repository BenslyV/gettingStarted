# Python If ... Else
a = 5
b = 7
if a == b:
    print("A is equal to b")
elif a > b:
    print("A is greater than B")
else:
    print("A is less than B")

# Short Hand If

if a > b: print("A is grater than B")

a = 2
b = 330
print("A") if a > b else print("B")

# Python While Loops

i = 6
while i > 0:
    print(i)
    i = i - 1

# Python For Loops

fruits = ['Banana', 'Apple', 'Orange']
print(type(fruits))
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print("Continue Statement")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function

for x in range(10):
    print(x)

# Check the number is odd or even

num = input("Enter the number")
if int(num) % 2 == 0:
    print(" The number is a even number")

else:
    print("the number is odd number")

# else if

age = int(input("Enter the age"))
if age < 5:
    print("Pay 30 rs for ticket")
elif age <= 5:
    print("Pay 50 rs for ticket")
elif 18 <= age <= 70:
    print("Pay Rs 100 for ticket")
else:
    print("You are not allowed")
