# Practice Problem: Ask the user for a sentence. Replace every empty space in that sentence with an underscore (_) and print the final result.

# Given Input: "I love coding in Python"
# Expected Output: I_love_coding_in_Python

# input(), this can handle any sentence the user provides, making it a flexible utility script.
# inputValue = input("I love coding in Python")
inputValue = "I love coding in Python"

spaceReplace = inputValue.replace(" ", "_")

print(spaceReplace)
