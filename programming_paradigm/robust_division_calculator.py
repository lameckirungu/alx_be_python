def safe_divide(numerator, denominator):
    try:
        res = numerator / denominator
        print(f"The result of the division is {res}")
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero")
    except ValueError:
        print(f"Error: Please insert a numeric values only.")

safe_divide()