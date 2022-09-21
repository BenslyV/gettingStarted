class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        print("Auto Called statement inside the init block")

    def print_name(self):
        print(f"Name of the person is {self.first_name} {self.last_name}")
        print("I am into parent class")

    def print_statement(self):
        print("Print statement of Parent")
        # print(f"Name of the person is {self.first_name} {self.last_name}")


student = Person(lname="Bensly", fname="V")
student.print_name()


class CollegeStudent(Person):

    def __init__(self, fullname):
        self.full_name = fullname

    def print_fullname(self):
        print(f"Class Student Class{self.full_name}")

    # def print_name(self):
    #     print(f"Name of the person is {self.first_name} {self.last_name}")
    #     print("I am in the child class")


coll_stu = CollegeStudent(fullname="Bensly Viswanathan")
# coll_stu.print_name()
# coll_stu.__init__("Bensly Viswanathan")
coll_stu.print_fullname()
coll_stu.print_statement()
coll_stu
