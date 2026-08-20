# Problem: 
# Write a program that takes a year as input and determines if it is a leap year.

# Given Input: year = 2024

# Expected Output: 2024 is a leap year

# Solution:

def leap_year(year):
  print("Input: year = ", year)
  if (year%4 == 0 and year%100 !=0) or (year%400 == 0):
    print(f"{year} is a leap year")
  else:
    print(f"{year} is not a leap year")

leap_year(2024)
leap_year(2025)
