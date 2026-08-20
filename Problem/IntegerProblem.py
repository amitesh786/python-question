# Problem: 
# Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product, otherwise, return their sum.

# Given Input:
# Case 1: number1 = 20, number2 = 30
# Case 2: number1 = 40, number2 = 30

# Expected Output:
# Result is: 600
# Result is: 70

# Solution:

def calculate_fn(num1, num2):
    product = num1 * num2
    if (product <= 1000):
        return product
    else:
        return num1 + num2

result1 = calculate_fn(20, 30)
print("Result is: ", result1)

result2 = calculate_fn(40, 30)
print("Result is: ", result2)
