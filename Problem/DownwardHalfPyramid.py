# Problem: 
# Print a downward half-pyramid pattern using stars (*).

# Given Input: Rows: 5

# Expected Output:
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# Solution:

for num in range(5, 0, -1):
  for i in range(0, num):
    print("*", end=" ")
  print("\n")
