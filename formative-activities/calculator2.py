# Function definitions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Loop will run till user exits
while True:

    # Gets user input and handles invalid input
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input")
        continue  # Restarts loop if input is invalid

    # Shows user menu options
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Gets users choice
    choice = input("\nEnter choice: ")

    # Variables for result and operation symbol
    result = None
    symbol = ""

    # Performs selected operation
    if choice == "1":
        result = add(x, y)
        symbol = "+"
    elif choice == "2":
        result = subtract(x, y)
        symbol = "-"
    elif choice == "3":
        result = multiply(x, y)
        symbol = "*"
    elif choice == "4":
        if y == 0:
            print("Cannot divide by zero")
        else:
            result = divide(x, y)
            symbol = "/"
    else:
        print("Invalid choice")

    # Displays result if valid operation performed
    if result is not None:
        print(f"Result: {x} {symbol} {y} = {result}")

    # Asks user if they want to continue
    again = input("\nWould you like to continue? (y/n): ")
    if again.lower() == "n":
        break  # Exists loop