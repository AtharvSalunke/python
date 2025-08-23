

class domainexpansion:
    def __init__(self,owner,name,power,duration):
        self.owner = input(f"Enter the owner of this DE: {owner}")
        self.name = input(f"Enter the name: {name}")
        self.power = input(f"Enter the power: {power}")
        self.duration = input(f"Enter the time: {duration}")

    def __str__(self):    # only returns strings in human readable format
        return (
            f"============= {self.owner}'s Data ===========\n"
            f"Owner: {self.owner}\n"
            f"Name: {self.name}\n"
            f"Power: {self.power}\n"
            f"Duration: {self.duration}\n"
        )

object = domainexpansion("","", "", "")
print(object)


# __init__ is like a constructor
# whenever an object is created from a class, the __init__ method is called automatically