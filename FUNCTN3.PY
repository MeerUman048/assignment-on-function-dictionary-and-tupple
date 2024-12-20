#WITHOUT USING GLOBAL KEYWORD
counter = 0

def increment_counter():
    counter = counter + 1  # Attempt to increment counter
    print(f"Counter inside function: {counter}")

# Calling the function multiple times
increment_counter()  # This will cause an error
increment_counter()



