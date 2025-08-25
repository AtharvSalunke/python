# try in a try block and except in a except block


x = 69

try:
    print(f"this is {x}")

    try:
        print("this is executed")
        
    except:
        print("Not executed")
        
except NameError:
    print("no variable defined")   # only this will execute if exception occurs


  
