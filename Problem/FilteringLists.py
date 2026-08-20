# Problem: 
# Iterate through a given list of numbers and print only those numbers which are divisible by 5.

# Given Input: num_list = [10, 20, 33, 46, 55]

# Expected Output:

# Divisible by 5:
# 10, 20, 55

# Solution:

num_list = [10, 20, 33, 46, 55]
print("Given list is", num_list)
print("Divisible by 5:")

for num in num_list:
    if num % 5 == 0:
        print(num)
