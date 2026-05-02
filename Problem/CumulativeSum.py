# Problem: 
# Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

# Given Input: Range: numbers = range(10)

# Expected Output:

# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number 0 Sum: 0
# Current Number 1 Previous Number 0 Sum: 1
# Current Number 2 Previous Number 1 Sum: 3
# ....
# Current Number 8 Previous Number 7 Sum: 15
# Current Number 9 Previous Number 8 Sum: 17

# Solution:

def print_sum():
    print("Printing current and previous number sum in a range(10)")
    previous_num = 0
    
    for current_num in range(10):
        total = current_num + previous_num
        print(f"Current Number {current_num} Previous Number {previous_num} Sum: {total}")
        previous_num = current_num

print_sum()
