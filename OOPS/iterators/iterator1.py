class IteratorExample:
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.count = 0   # keep track of iteration

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count == 0:
            self.count += 1
            return self.name
        elif self.count == 1:
            self.count += 1
            return self.age
        else:
            raise StopIteration   # stop iteration
        

obj = IteratorExample()

for value in obj:   # iterates automatically
    print(value)
