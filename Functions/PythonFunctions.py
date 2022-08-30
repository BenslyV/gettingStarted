import math


def my_function(a, b):
    print(f"Hello, I am  calculating the sum of {a} and {b}")
    c = int(a) + int(b)
    print(f"Sum is {int(c)}")


my_function(19, 25)

L1 = [40, 15, 24, 70]
print(L1)

print(math.factorial(5))


# Factorial of a number

def fact(n):
    num = n
    factorial = 1
    if num < 0:
        print(" Factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)

    return factorial


fact(5)


def func(x, y=1):
    z = x * y + x + y
    return z


# func(2, func(3))

# Lamda function


a1 = lambda num: "Even" if num % 2 == 0 else "Odd"

print(a1(10))

min = (lambda x, y: x if x < y else y)
print(min(101 * 99, 102 * 98))


# Greet function

def greet(name, location):
    print(f"Hello {name}")
    print(f"How r u {name}")
    print(f"Are you familiar with Python")
    print(f"Your are from {location}. Right?")


greet(location='TVM', name='Bensly')

# paint area calculator

print("Welcome to paint Calculator")
height = int(input(f"Enter the height"))
width = int(input(f"Enter the width"))


def paint_area(height, width, coverage=5):
    area_painted = int( height * width % coverage)
    return area_painted


paint_area(height, width,5)
