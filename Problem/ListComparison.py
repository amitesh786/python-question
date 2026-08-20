# Problem: 
# Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

# Given Input:

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# Expected Output:

# Given list: [75, 65, 35, 75, 30] | result is False
# Given list: [10, 20, 30, 40, 10] | result is True

# Solution:

def first_last_num(number_list):
  print("Given list:", number_list)

  first_num = number_list[0]
  last_num = number_list[-1]

  if first_num == last_num:
    return True
  else:
    return False
  
print("result is", first_last_num([75, 65, 35, 75, 30]))

print("result is", first_last_num([10, 20, 30, 40, 10]))
