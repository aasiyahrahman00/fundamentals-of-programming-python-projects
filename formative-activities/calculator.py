# Printing Hello World
print("Hello World")

# Asking for two numbers
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# Print numbers entered
print(f"You entered: {num1} and {num2}")

print("Results:")

# Addition of numbers entered
addition = num1 + num2
print(f"{num1} + {num2} = {addition}")

# Subtraction of numbers entered
subtraction = num1 - num2
print(f"{num1} - {num2} = {subtraction}")

# Multiplication of numbers entered
multiplication = num1 * num2
print(f"{num1} * {num2} = {multiplication}")

# Division of numbers entered
if num2 == 0:
    print("Cannot divide by zero")
else:
    division = num1 / num2
    print(f"{num1} / {num2} = {division}")