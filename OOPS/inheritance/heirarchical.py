# multiple child and single parent
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child1(Parent):
    def intro1(self):
        print("I am Child1")

class Child2(Parent):
    def intro2(self):
        print("I am Child2")

obj1 = Child1()
obj2 = Child2()
obj1.greet()
obj2.greet()
