cars = ["Ford", "Volvo", "BMW"]
print(type(cars))
print(cars[0])
print(len(cars))

# Looping in array
for x in cars:
  print(x)

# Adding Array Elements
cars.append("Honda")
print(cars)


#Delete the second element of the cars array:
cars.pop(2)
print(cars)