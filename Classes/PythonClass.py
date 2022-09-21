import TurtleProject


def fun(in1, in2):
    print("This is my function")
    a = in1
    b = in2
    c = in1 + in2
    return c


class Amsikkakuzhi:
    x = 5

    def __init__(self, a , b):
        self.num1 = a
        self.num2 = b



    @staticmethod
    def church():
        print("CSI Amsikkakuzhi is my Church")

    # print(x)

    @staticmethod
    def gym():
        print("No Gym in Amsikkakuzhi")

    def meth(self):
        print("This is a method")

    # print(x)

    @classmethod
    def myClassMethod(cls):
        print("This is a Class Method")
    # print(x)


place = Amsikkakuzhi()
print(place.x)
place.church()
print(fun(40, 50))
place.gym()
place.church()
Amsikkakuzhi.gym()
# Amsikkakuzhi.meth(4)
place.meth()

# TurtleProject.table
place.myClassMethod()


class Car:
    def sound(self):
        print("Vroooom!")


ferrari = Car()
ferrari.sound()  # calling method sound on object ferrari

f = Car()

class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance variables
    def show(self):
        print(self.name, self.age, Student.school_name)

    @classmethod
    def change_School(cls, name):
        cls.school_name = name

    @staticmethod
    def find_notes(subject_name):
        return ['chapter 1', 'chapter 2', 'chapter 3']


print(Student.school_name)
st1 = Student("Ram", 12)
st1.show()


class Person():
    def __init__(self, name, age):
        self.myname = name
        self.myage = age

    def numAdd(self):
        stu2 = Person("Raj", 45)

        age1 = stu2.myage
        print(f"My age is {age1}")


stu1 = Person("Bensly", 15)
print(stu1.myname)
Person.numAdd("Raj")


class HelloWorld:
    str1 = 15

    def __init__(self, str):
        self.name = str
        str2 = 15

    def javaAdd(self, a, b):
        num = a + b
        print("This is Java from Hello world")
        print(num)
        print(self.name)
        print(HelloWorld.str1)
        print(HelloWorld)

    def pythonSub(self):
        print("This is Python from Hello world")


hw = HelloWorld("Bensly")
hw.javaAdd(13, 24)
print(hw.str1)
