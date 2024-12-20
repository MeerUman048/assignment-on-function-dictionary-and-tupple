#Use the math module to write a function rhombus_area that calculates the area of a RHOMBUS?
import math

def rhombus_area(d1, d2):
    return (1/2) * d1 * d2

# Example usage:
diagonal1 = 10
diagonal2 = 6
area = rhombus_area(diagonal1, diagonal2)
print(f"The area of the rhombus is: {area}")
