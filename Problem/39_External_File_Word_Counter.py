# Practice Problem: Write a script that opens an existing .txt file and counts the total number of words it contains.

# Given Input:
# An external file sample.txt containing: “Coding is the language of the future.”
# Expected Output: The file contains 7 words.

try:
  with open("sample.txt", "r") as file:
    data = file.read()
    words = data.split()
    word_count = len(words)
    print(f"The file contains {word_count} words.")
except FileNotFoundError:
  print("Error: The file 'sample.txt' was not found.")

