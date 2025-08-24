

class A:
    def method(self):
        print("Class A")

class B(A):
    def method(self):
        print("Class B")

class C(A):
    def method(self):
        print("Class C")

class D(B, C):  # Hybrid: multiple + hierarchical
    pass

obj = D()
obj.method()   # MRO decides -> Class B
print(D.mro())  # Shows resolution order
