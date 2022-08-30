# Python Strings
print("Hello")
print('Hello')
a = 'hello string'
print(a)

b = 'hello, world 2'
print(b[2])

for x in "banana":
    print(x)

    a = "Hello, World!"
    print(len(a))

    print(len(b))

txt = "The best things in life are free!"
print('free' in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

if 'best' in txt:
    print("yes, it is present")

    print('hello' not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Slicing strings
print(txt[5:15])

# Slice From the Start
print(b[:5])
# Slice To the End
b = "Hello, World!"
print(b[2:])

b1 = 'hello world'
print(b1.upper())
b2 = print(b1.upper())
#print(b2.islower())

a = "Hello, World!"
print(a.replace("H", "J"))
print(a.split(','))

print(a.capitalize())

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#String Format
age = 36
txt1 = "My name is John, I am {}" # + age
print(txt1)
print(txt1.format(age))

quantity = 3
itemno = 567
price = 49.95

myorder="I want item number {} of {} for the price of{}"
print(myorder.format(quantity , itemno , price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt2 = "We are the so-called \"Vikings\" \n from\tthe\t\\'north."
print(txt2)
#String Methods
print("String Methods running")
print(txt2.count('are'))
#print(txt2.translate())



#Python booleans

print(10 > 9)
print(10 == 9)
print(10 < 9)

m=50
n=60
if m>n:
    print( " M is greater than n")
else:
    print("n is grater than m")

print(bool("Hello"))
print(bool(0))

class gettingStarted():
  def  test1(self):
      return True
  print("Returning Test1 function")
  print(test1())




