# update , pop, del


dict1 = {
    "EMP_ID": 1089,
    "NAME": "Atharv Salunke",
    "SALARY": 8900000,
    "JOB": "Software Developer"
}


dict1.update({"LOCATION": "PUNE"})
print(dict1)



dict1.pop("LOCATION")
print(dict1)


del dict1["NAME"]
print(dict1)