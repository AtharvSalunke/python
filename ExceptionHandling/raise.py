# to throw an exception to a condition we use raise keyword

# raise always needs a condition


x = 100
try:
    print(f"x is {x}")

    if x > 50:
        raise ValueError("x should not be more than 50")
except ValueError as e:
    print("Caught an error:", e)
