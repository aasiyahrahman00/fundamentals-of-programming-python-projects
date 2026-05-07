# Variable and Control Flow Exercise: Age Checker
while True:
    try:
        age = int(input("How old are you?"))
        if age < 18:
            print("\nYou are a minor")
        else:
            print("\nYou are an adult")
        break
    except ValueError:
        print("\nInvalid input! Enter a number")



# Basic Function Exercise: Sum Calculator
def calculate_sum(num1, num2):
    return num1 + num2

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

result = calculate_sum(num1, num2)
print(f"Your sum is {result}")


# List Operation Exercise: List Doubler
numbers = [2, 4, 6, 8, 10]

for num in numbers:
    doubled = num * 2
    print(f"The list doubled is {doubled}")