num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

user_operator = input("Choose the operation (+, -, *, /): ")

if user_operator == '/' and num2 == 0:
    print("Cannot divide by zero.")
else:
    match user_operator:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            result = num1 / num2
            print(f"The result is {result}.")
        case _:
            print("Invalid operator")
