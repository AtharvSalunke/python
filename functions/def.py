def calculator():
    x = int(input("Enter the data1: "))
    y = int(input("Enter the data2: "))

    while True:
        print('1. +')
        print('2. -')
        print('3. *')
        print('4. /')
        print('5. Exit')
        ch = input("Enter your choice: ")

        if ch == '1':
            print(f"Result: {x + y}")
        elif ch == '2':
            print(f"Result: {x - y}")
        elif ch == '3':
            print(f"Result: {x * y}")
        elif ch == '4':
            if y != 0:
                print(f"Result: {x / y}")
            else:
                print("Cannot divide by zero!")
        elif ch == '5':
            print("Exiting the calculator")
            break
        else:
            print("Invalid choice, please try again.")

calculator()
