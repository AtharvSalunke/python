# union, update, intersection, difference

set1= {1,2,3,4}
set2 = {4,5,6,7}

a = set1.union(set2)
print(a)                      # no double data displayed 

b = set1.intersection(set2)
print(b)

c = set1.difference(set2)   # return only those data from set1 which are not from set2
print(c)

d = set2.difference(set1) # returns only those data from set2 which are not from set1
print(d)

e = set1.symmetric_difference(set2)
print(e)                          # same answer as (f)

f = set2.symmetric_difference(set1)
print(f)