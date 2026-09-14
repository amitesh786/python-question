# Problem: Write a Python program that accepts a user’s name as input and writes it to a file called user.txt.

# Given Input: User enters their name at runtime, e.g. Alice
# Expected Output: A file named user.txt is created containing the entered name, e.g. Alice

name = input("Enter your name: ")

with open("user.txt", "w") as file:
  file.write(name)

print("Name written to user.txt")
