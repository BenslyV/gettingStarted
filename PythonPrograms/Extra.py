tuple = (2,3.2,4,5)
print(min(tuple))
print(max(tuple))
print((sum(tuple)))

t = ("disco", 12, 4.5)
print(t[0][2])

t = (1, 2, 4, 3)
print(t[3])

input_tuple = ('Monty Python', 'British', 1969)
print(input_tuple)

input_list = list(input_tuple)
print(type(input_list))
print(input_list)

input_list.append("Python")

print("Printing the List")
print(input_list)

print("Printing the Tuple")
#tuple_2 = tuple(input_list)
print(type(input_tuple))

l= [1,2,"stackoverflow","python"]
#tup = tuple(l)
#print(type(tup))

# Sets
# print(("We are in set"))
#
# import ast,sys
# input_str = sys.stdin.read()
# input_list = ast.literal_eval(input_str)
# list_1 = input_list[0]
# list_2 = input_list[1]
#
# print(list_1)
# print(list_2)
#
# #Type your answer here
#
# set1 = set(list_1)
# set2 = set(list_2)
# answer = set1.intersection()
# answer = list(answer)
# print(answer)


d = {"India" : "INR", "USA" : "USD", "France" : "Euros"}

print(sorted(d.values()))

a={1,2,3,5,6,7}
b={4,5,8,9,2,3}

a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)


# Create a dictionary:
dir = {"Sam": 21,
"Cody": 12,
"Addy": 3,
"Zach": 45,
"Amy": 6
      }

# Print the result:
print(type(dir))
print(dir)


print("employee data with key as id of the employee and values as age of the employee")
Employee_data ={101: 43, 102: 25, 103: 43, 104: 31, 105: 26, 106: 28, 107: 29, 108: 43, 109: 25, 110: 22, 111: 22, 112: 25,
                113: 30, 115: 45, 116: 23, 117: 29, 118: 28, 119: 30, 120: 28, 121: 42, 122: 39, 123: 29, 124: 42, 125: 43,
                126: 42, 127: 40, 128: 27, 129: 23, 130: 30, 131: 37, 132: 20, 133: 36, 134: 27, 135: 27, 136: 22, 137: 28,
                138: 23, 139: 45, 140: 39, 141: 29, 142: 33, 143: 39, 145: 34, 146: 26, 147: 30, 148: 38, 149: 29, 150: 24,
                151: 28, 152: 34, 153: 42, 154: 29, 155: 23, 156: 31, 158: 25, 160: 45, 161: 42, 162: 27, 163: 24, 164: 20,
                166: 24, 167: 28, 168: 20, 169: 33, 170: 34, 171: 37, 172: 45, 173: 35, 174: 23, 175: 44, 176: 27, 177: 30, 178: 26, 179: 27}
print(max(Employee_data.values()))

print(Employee_data.keys("159"))