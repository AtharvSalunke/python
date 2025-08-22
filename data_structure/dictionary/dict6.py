# nested dictionary

dict1 = {
    "EMPLOYEES":{
    "EMP_ID": 1089,
    "NAME": "Atharv Salunke",
    "SALARY": 8900000,
    "JOB": "Software Developer"
}, 

   "Students":{
    "name":'rajesh',
    "age": 21,
    "location": 'pune'
},
   "CAR": {
       "BRAND": "Toyota",
       "MODEL": "Camry",
       "YEAR": 2020
   }
}


for x in dict1["EMPLOYEES"]:
    print(dict1["EMPLOYEES"][x])


for sections in dict1:
    print(f"{sections}:")
    for key, value in dict1[sections].items():
        print(f"  {key}: {value}")
    print()