# single inheritance means single parent

class A:
    def __init__(self):
        self.name = input("Enter name: ")
        self.property = input("Enter property: ")

    def display(self):
        print(f"name is {self.name}")
        print(f"property is {self.property}")


class B(A):
    def __init__(self):
        super().__init__()
        self.extra = input("Enter extra: ")

    def show(self):
        print(f"extra is {self.extra}")


obj = B()
obj.display()
obj.show()
