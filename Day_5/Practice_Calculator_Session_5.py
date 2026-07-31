# Functions for Operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None


# Input & Validation Functions
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_operator():
    valid_operators = {"+", "-", "*", "/"}
    while True:
        oper = input("Please enter an operator (+, -, *, /): ").strip()
        if oper in valid_operators:
            return oper
        print("Invalid operator! Please enter one of (+, -, *, /).")


# Main calculator
def calculator():
    print("### Wellcome TO Calculator ###")

    first = get_number("Please enter the first number: ")
    oper = get_operator()
    second = get_number("Please enter the second number: ")

    result = None

    if oper == "+":
        result = add(first, second)
    elif oper == "-":
        result = subtract(first, second)
    elif oper == "*":
        result = multiply(first, second)
    elif oper == "/":
        result = divide(first, second)

    if result is not None:
        # if number is whole, show as integer
        if result.is_integer():
            result = int(result)

        print(f"\nResult: {first} {oper} {second} = {result}")


# Run the calculator
if __name__ == "__main__":
    calculator()
