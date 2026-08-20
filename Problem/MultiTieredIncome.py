# Problem: 
# Calculate income tax for a given income based on these rules:

# First $10,000: 0% tax
# Next $10,000: 10% tax
# Remaining income: 20% tax

# Given Input: income = 45000

# Expected Output: Total income tax to pay is 6000

income = 45000
tax_payable = 0
print("Input: income = ", income)

if income <= 10000:
  tax_payable = 0
elif income <=20000:
  tax_payable = (income - 10000) * 10 / 100
else:
  tax_payable = 0 + (10000 * 10 / 100) 
  tax_payable += (income - 20000) * 20 / 100

print("Output: Total income tax to pay is ", tax_payable)
