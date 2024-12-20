# Q:Create a tuple of 5 random numbers. Check if a specific number (e.g., 7) exists in the tuple. Print an appropriate msg?
import random

# Generate a tuple of 5 random numbers between 1 and 10
random_numbers = tuple(random.randint(1, 10) for _ in range(5))
print(f"Generated tuple: {random_numbers}")

# Check if the number 7 is in the tuple
if 7 in random_numbers:
    print("The number 7 is in the tuple.")
else:
    print("The number 7 is not in the tuple.")
