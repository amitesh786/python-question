# Problem: 
# Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

# Given Input:

# Case 1: number = 121
# Case 2: number = 125
# Expected Output:

# Number 125 is not palindrome number
# Number 121 is palindrome number

# Solution:

def num_palindrome(number):
  original_str = str(number)
  reversed_str = original_str[::-1]

  if original_str == reversed_str:
    print(f"Number {number} is palindrome number")
  else: 
    print(f"Number {number} is not palindrome number")
  
num_palindrome(121)
num_palindrome(125)
