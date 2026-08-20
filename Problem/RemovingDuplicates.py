# Problem: 
# Write a script that takes a list containing duplicate items and returns a new list with only unique elements.

# Given Input: data = [1, 2, 2, 3, 4, 4, 4, 5]

# Expected Output: Unique List: [1, 2, 3, 4, 5]

# Solution:

data = [1, 2, 2, 3, 4, 4, 4, 5]

unique_data = list(set(data))

print(f"Unique List: {unique_data}")
