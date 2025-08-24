

class domainexpansion:
    def __init__(self,owner,name,power,duration):
        self.owner = input(f"Enter the owner of this DE: {owner}")
        self.name = input(f"Enter the name: {name}")
        self.power = input(f"Enter the power: {power}")
        self.duration = input(f"Enter the time: {duration}")

    def display(self):
        print(f"============= {self.owner}'s Data ===========")
        print(f"Owner: {self.owner}")
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Duration: {self.duration}")

object = domainexpansion("","", "", "")

object.display()


# __init__ is like a constructor
# whenever an object is created from a class, the __init__ method is called automatically