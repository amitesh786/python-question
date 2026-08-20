# Problem: 
# Write a program to check if a given number is a palindrome. A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

# Exercise Purpose: This exercise teaches “Algorithmic Reversal.” While strings are easy to reverse in Python, reversing a number mathematically using the modulo (%) and floor division (//) operators deepens understanding of how integers are stored in memory and how to manipulate digits individually.

# Given Input: number = 121

# Expected Output:

# Original number 121
# Yes. given number is palindrome number

# Solution:

# number = 121
# print(f"Original number: {number}")

# number_str = str(number)
# reversed_str = number_str[::-1]

# if number_str == reversed_str:
#   print(f"Yes. given number is palindrome number")
# else:
#   print(f"No. given number is not palindrome number")

number = 121
print("Given Number:", number)
original_number = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

if reversed_number == original_number:
  print(f"Yes. given number is palindrome number")
else:
   print(f"No. given number is not palindrome number")
