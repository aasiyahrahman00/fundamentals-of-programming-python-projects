# Global variable
counter_one = 0

#  Function that accesses and modifies the global variable
def increment():
    global counter_one # Declare we want to use the global counter
    counter_one += 1
    print(f"Inside increment function using a global function, counter_one: {counter_one}")

# Function that creates a local variable
def decrement():
    counter_two = 0  # Local variable
    counter_two -= 1
    print(f"Inside decrement function using a local variable, counter_two: {counter_two}")

# Function that changes the global variable
def counter_change():
    global counter_one
    counter_one = 10
    print(f"Inside counter_change function, counter_one is set to ten: {counter_one}")

print(f"Global variable, counter_one: {counter_one}")   # Helps to compare values before and after function runs
increment()   # Shows function can access and modify the global variable
decrement()   # Shows local variable exists only inside the function
print(f"Printing global variable from outside the function: {counter_one}")   # Shows local variable exists only inside function
counter_change()   # Shows the global variable value changes everywhere after update
print(f"Global variable, counter_one: {counter_one}")   # Shows global variable stayed changed after the function ended