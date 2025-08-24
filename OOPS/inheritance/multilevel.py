# multilevel inheritance means having a parent and grandparent

class Grandparent:
    def origin(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def role(self):
        print("I am Parent")

class Child(Parent):
    def identity(self):
        print("I am Child")

obj = Child()
obj.identity()
