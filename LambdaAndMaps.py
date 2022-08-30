# Lamda function


a1 = lambda num: "Even" if num % 2 == 0 else "Odd"


print(a1(10))

min = (lambda x, y: x if x < y else y)
print(min(101*99, 102*98))


# Maps

print("We are in the maps")
l = [1, 2, 3, 4, 5]
fun = lambda mul: mul*5

print(list(map(fun,l)))