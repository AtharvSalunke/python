# finding smallest number in list

list1 = [123,1232,4,345,546,4232]

minvalue = list1[0]

for i in list1:
    if i < minvalue:
        minvalue = i

print(minvalue)


# TC is O(n) because no of elemts = no of loops it will take