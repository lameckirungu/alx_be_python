import sys

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
       
user_operator = input("Choose the operation (+, -, *, /): ")
if num2 == 0 and user_operator == '/':
    print("Cannot divide by zero.")
    sys.exit(1)

match user_operator:
    case '+':
       result = num1 + num2
    case '-':
       result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        result = num1 / num2
    case _:
        print("Invalid operator.")
        sys.exit(1)
    
print(f"The result is {result}.")