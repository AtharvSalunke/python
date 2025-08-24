# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.



try:
    global x
    x = 5
    print("this is try block")
    print(f"the number is {x}")

except:

    print("this is except block\n when there is error it handles it")
    print("undefined variable")




# when u remove x = 5 then it will run except block