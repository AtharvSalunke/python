# iterator is used to accesss each and every elemnts in
# collections like list , tuples , dictionaries.
# instead of using indexes we can use iterators

# iterators are the objects which allow us to traverse
# through a collection

# it remembers its state and can be be used to acess the
# next element using next()


list1 = [1,2,3,4,"apple"]


x = iter(list1)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))