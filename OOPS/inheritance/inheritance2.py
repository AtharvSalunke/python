
# Python also has a super() function that will make 
# the child class inherit all the methods and properties 
# from its parent:

# By using the super() function, you do not have to 
# use the name of the parent element, it will automatically 
# inherit the methods and properties from its parent.




class base:
    def __init__(self,name):
        self.name = input("name: ")

    def display(self):
        print(f"========= ")
        print(f"name is {self.name}")


class derived(base):
    def __init__(self,name):
        super().__init__(name)


p1 = derived(" ")
p1.display()