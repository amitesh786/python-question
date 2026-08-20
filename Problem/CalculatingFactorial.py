# Problem: 
# Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.

# Given Input: number = 5

# Expected Output: The factorial of 5 is 120

# Solution:

num = 5
fact = 1

for i in range(1, num + 1):
  fact = fact * i

print(f"The factorial of {num} is {fact}")
