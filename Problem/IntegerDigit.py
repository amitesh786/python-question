# Problem: 
# Write a program to extract each digit from an integer in the reverse order.

# Exercise Purpose: This exercise explores “Mathematical Parsing.” Instead of converting a number to a string, use the modulo operator (%) and floor division (//) to isolate digits. This is common in low-level programming and algorithm challenges where type conversion is restricted.

# Given Input: number = 7536

# Expected Output: 6 3 5 7

# Approach 1: 
number = 7536
print(f"Input: number = {number}")

number_str = str(number)
reversed_str = number_str[::-1]

spaced_output = " ".join(reversed_str)
print(f"Output: {spaced_output}")

# Approach 2: 
number = 7536
print("Given Number:", number)

while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end=" ")
