# we can also define multiple except blocks




x = 1000
try:
    print(x)

except NameError:
    print("no variable")

except:
    print("dont know whats the error")

