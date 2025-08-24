# parent class and child class


class Parent:
    def __init__(self,name,age):         # self refers to the instance of a class
        self.name = input("name: ")
        self.age = input("age: ")

    def display(self):
        print(f"========= {self.name}'s data =============")
        print(f"name is {self.name}")
        print(f"age is {self.age}")


p1 = Parent("","")
p1.display()


class child(Parent):
    def __init__(self,name,age):
        self.name = input("child name: ")
        self.age = input("child age")
        

s1 = child("","")
s1.display()

# child class of parents can use its functions and properties

# Single Inheritance → 1 parent → 1 child

# Multiple Inheritance → 2+ parents → 1 child

# Multilevel Inheritance → Grandparent → Parent → Child

# Hierarchical Inheritance → 1 parent → 2+ children

# Hybrid Inheritance → Combination of two or more types