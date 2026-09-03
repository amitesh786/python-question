# Practice Problem: Write a program to capitalize the first letter of each word in a given string without using the built-in .title() method.

# Given Input: text = "hello world from python"

# Expected Output: Hello World From Python

text = "hello world from python"
input_text = text.split()
cap_array = []

for input in input_text:
  cap_array.append(input.capitalize())

result = " ".join(cap_array)
print(result)
