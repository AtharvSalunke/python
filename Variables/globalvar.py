x = 100

def addition():
    print(x + 900)

addition()                                          # this is normal 



def multiply():
    global x              # this var x becomes global. we can aslo print it outside the function too
    x = 20

    print(x * x)

multiply()



print(x)



