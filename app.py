def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Error! Division by zero.")
    return a / b

def percentage(a, b):
    if b == 0:
        return "Error! Division by zero."
    return (a / b) * 100

def calculator():
    """
    A simple calculator function that allows the user to perform basic arithmetic operations.

    The user is prompted to select an operation from the following:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Percentage

    The function then takes two numeric inputs from the user and performs the selected operation.
    It handles invalid inputs and division by zero gracefully.

    Returns:
        None

    Raises:
        ValueError: If the user inputs non-numeric values for the numbers.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
        elif choice == '5':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                print(f"The result is: {percentage(num1, num2)}%")
    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()