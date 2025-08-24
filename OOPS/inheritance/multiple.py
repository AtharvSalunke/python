# mutiple inheritance means having mutiple parents


class parent1():
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")

    def display1(self):
        print(f"name is  {self.name}")
        print(f"age is {self.age}")
 

class parent2():
    def __init__(self):
        self.gender = input("Gender: ")
        self.married = bool(input("Married? [True/False]: "))

    def display2(self):
        print(f"Gender is {self.gender}")
        print(f"Married??????  {self.married}")


class Child(parent1,parent2):
    def __init__(self):
        parent1.__init__(self)
        parent2.__init__(self)

    def display_all(self):
        self.display1()
        self.display2()# mutiple inheritance means having mutiple parents


class parent1():
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")

    def display1(self):
        print(f"name is  {self.name}")
        print(f"age is {self.age}")
 

class parent2():
    def __init__(self):
        self.gender = input("Gender: ")
        self.married = bool(input("Married? [True/False]: "))

    def display2(self):
        print(f"Gender is {self.gender}")
        print(f"Married??????  {self.married}")


class Child(parent1,parent2):
    def __init__(self):
        parent1.__init_(self)
        parent2.__init__(self)

    def display_all(self):
        self.display1()
        self.display2()




obj = Child()
obj.display_all()





obj = Child()
obj.display_all()
