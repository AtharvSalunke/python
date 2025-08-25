# finally - wether your try or except block is 
# right or wrong , does not matter, finally block executes

x = 1190   # you can add or remove this part to see the changes

try:
    print(f"this is {x}")

except NameError:

    print("variable deos not exists")

else:
    print("Sucessfully executed")

finally:
    print("This is Finally block")