
# lists - mutable ,  heterogeneous data, closed in [], it allows duplicate data 

y = [1,2,3,4]
y[0] = 1000
print(y)


list1 = ["apple",1,2,3, 'orange' ]

print(list1[0])
print(list1[2])
print(len(list1))

def listops():
    n = int(input("Enter the number of elements you want in the list: "))
    list2 = []

    for i in range(n):
        item = input(f"Enter element {i + 1}: ")
        list2.append(item)

    print("Final List:", list2)
    return list2


# Call the function
listops()




y = [1,2,3,4]

