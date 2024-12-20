def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
print(calculate(5, 3, '+'))  # Output: 8
print(calculate(5, 3, '-'))  # Output: 2
print(calculate(5, 3, '*'))  # Output: 15
print(calculate(5, 3, '/'))  # Output: 1.6
print(calculate(5, 3, '^'))  # Output: Error: Invalid operator

        

