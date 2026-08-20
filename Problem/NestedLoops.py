# Problem: 
# Print the following pattern where each row contains a number repeated a specific number of times based on its value.

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# Given Input: Range: 1 to 5

# SoLution:

for num in range(1, 6):
  for i in range(num):
    print(num, end=" ")
  print("\n")
