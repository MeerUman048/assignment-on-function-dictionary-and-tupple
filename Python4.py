#USING THE GLOBAL KEYWORD
counter = 0

def increment_counter():
    global counter  # Declare counter as global
    counter = counter + 1  # Increment counter
    print(f"Counter inside function: {counter}")

# Calling the function multiple times
increment_counter()  # Counter inside function: 1
increment_counter()  # Counter inside function: 2
increment_counter()  # Counter inside function: 3

print(f"Counter outside function: {counter}")  # Counter outside function: 3
