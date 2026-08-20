# Problem: 
# Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.

# Given Input:

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# Expected Output: [25, 35, 40, 60, 90]

# Solution:

def merge_list(list1, list2):
  result_num = []

  for num in list1:
    if num%2 != 0:
      result_num.append(num)
    
  for num in list2:
    if num%2 == 0:
      result_num.append(num)
  
  return result_num

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))
