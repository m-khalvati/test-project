# Mult/Div Selection phase
print("Welcome, Please select an operation: 1. Multiplication 2. Division")
i = int(input("Please select an operation "))
if i == 1:
    print("You have selected Multiplication")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print(f"The result of multiplying {num1} and {num2} is: {result}")
elif i == 2:
    print("You have selected Division")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
