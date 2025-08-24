# module.py

def calculate(a, b):
    while True:
        try:
            op = input("Enter operation (+, -, *, /): ")
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            elif op == "/":
                return a / b
            else:
                print("Invalid operation. Please try again.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print("Error:", e)
