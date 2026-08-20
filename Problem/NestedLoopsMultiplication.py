# Problem: 
# Print a multiplication table from 1 to 10 in a formatted grid.

# Given Input: Range: 1 to 10

# Expected Output:

# 1  2  3  4  5  6  7  8  9  10 		
# 2  4  6  8  10 12 14 16 18 20 		
# ... (up to 10)

# Solution:

for i in range(1, 11):
  for j in range(1, 11):
    print(i * j, end="\t")
  print("\n")
