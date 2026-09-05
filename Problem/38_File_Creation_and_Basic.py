# Practice Problem: Write a program that creates a new text file named notes.txt, writes three separate lines of text to it, and then reads that file back to display the contents in the console.

# Given Input: Lines to write:

# “Hello, this is my first note.”
# “Python file handling is simple.”
# “End of file.”

# Expected Output:

# notes.txt

# Hello, this is my first note.
# Python file handling is simple.
# End of file.


# Part 1: Writing the file
with open("notes.txt", "w") as file:
  file.write("Hello, this is my first note.\n")
  file.write("“Python file handling is simple.\n")
  file.write("“End of file.\n")

# Part 2: Reading from the file
print("Reading file contents:")
with open("notes.txt", "r") as file:
  content = file.read()
  print(content)
