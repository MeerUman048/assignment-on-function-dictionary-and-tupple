#Q:Use the random module to write a function generate_random_numbers that generates 
#and returns a list of n random integers between a specified range a and b. 
import random

def generate_random_numbers(n, a, b):
    random_numbers = [random.randint(a, b) for _ in range(n)]
    return random_numbers

# Example usage:
n = 5  # Number of random integers
a = 1  # Start of the range
b = 10  # End of the range
random_numbers_list = generate_random_numbers(n, a, b)
print(random_numbers_list)  # Output: [random integers between 1 and 10]
