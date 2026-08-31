# Practice Problem: Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.

# Given Input: input_string = "Python3"

# Expected Output: The string 'Python3' contains digits: True

isFlag = False
input_string = 'Python3'

for char in input_string:
  if char.isdigit():
    isFlag = True
    break

print(f"The string '{input_string}' contains digits: {isFlag}")
