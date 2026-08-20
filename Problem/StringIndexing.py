# Problem: 
# Display only those characters which are present at an even index number in given string.

# Given Input: String: "pynative"

# Expected Output:

# Original String is  pynative
# Printing only even index chars
# p
# n
# t
# v

# Solution:

def print_even_index_chars(text):
  print("Original String is", text)
  print("Printing only even index chars")

  for i in range(len(text)):
    if i%2 == 0:
      print(text[i])
    
print_even_index_chars("pynative")
