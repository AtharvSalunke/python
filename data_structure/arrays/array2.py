array1 = [1,2,3,4,5]
array2 = ['apple', 'ball', 'cat']


array1.append(100000000)
print(array1)

array1.insert(1, array2)
print(array1)


array2.pop()
print(array2)

array2.pop(1)
print(array2)