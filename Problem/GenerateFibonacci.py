# Problem: 
# Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

# Given Input: Terms = 15

# Expected Output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# Solution:

num1, num2 = 0, 1
print("Fibonacci series:")

for i in range(4):
    print(num1, end="  ")

    res = num1 + num2
    num1 = num2
    num2 = res

    print(num1)
    print(num2)
