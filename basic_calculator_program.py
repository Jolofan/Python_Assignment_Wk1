print("Welcome to the Basic Python Calculator")

# For user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /)")

# Calculation
if operation == '+':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif operation == '/':
    if num2 == 0:
        print("\nError: Division by zero (0) is NOT allowed! ❌")
    else:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")

else:
    print("\nInvalid operation! Enter +, -, *, or / Only.")

print("\nThank you for using the calculator! Buy some water! ")
