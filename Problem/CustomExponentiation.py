# Problem: 
# Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

# Given Input: base = 2, exp = 5

# Expected Output: 2 raises to the power of 5: 32

# Solution:

def exponent(base, exp):
    num = exp
    result = 1

    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is:", result)

exponent(2, 5)
exponent(5, 4)
