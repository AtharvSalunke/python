dict1 = {
    "name": 'Atharv',
    "age":23,
    "location": 'pune'
}
for key in dict1.keys():
    print(key)
print("____________________________________________")
for values in dict1.values():
    print(values)
print("____________________________________________")

for key, values in dict1.items():
    print(key,values)