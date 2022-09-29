x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = pow(4, 3)

print(x)

import math as m

print(m.sqrt(64))
print(m.ceil(5.6))
print(m.floor(3.2))
print(m.pi)

import json as j

# some JSON:
x1 = '{ "name":"John", "age":30, "city":"New York"}'
y = j.loads(x1)
print(y)
print(type(y))

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# a Python object (dict):
x2 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y2 = j.dumps(x2)

# the result is a JSON string:
print(y2)
print(type(y2))

import camelcase as cc

c = cc.CamelCase()
txt = "hello world"
print(c.hump(txt))

jo = j.JSONDecoder()
jo1 = j.JSONDecoder
print(jo1)
print("printing variables")
print(m.e)
print(m.inf)
print(m.nan)

import selenium as sel

