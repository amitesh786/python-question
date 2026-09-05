# Practice Problem: Create a countdown timer that starts from a given number and counts down to zero using a while loop.

# Given Input: start_count = 5
# Expected Output: 5 4 3 2 1 Blast off!

import time

start_count = 5

while start_count > 0:
  print(start_count)

  time.sleep(1)

  start_count -= 1

print("Blast off!")
