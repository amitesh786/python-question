# Problem: 
# Write a program to swap the values of two variables, a and b, without using a third temporary variable.

# Given Input: a = 5, b = 10

# Expected Output:

# Before Swap: a = 5, b = 10
# After Swap: a = 10, b = 5

# Solution:

def swap_values(a, b):
    print(f"Before Swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After Swap: a = {a}, b = {b}")

swap_values(5, 10)
