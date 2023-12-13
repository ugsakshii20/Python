def print_alphabet_pyramid(rows):
  """
  This function prints an alphabet pyramid pattern with the given number of rows.
  """
  start_char = ord('A')
  for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
      print(" ", end="")
    # Print characters
    for j in range(i):
      char = chr(start_char + j)
      print(char, end="")
    # Print characters in reverse order
    for j in range(i - 2, -1, -1):
      char = chr(start_char + j)
      print(char, end="")
    print()

# Define the number of rows
rows = 5

# Print the pyramid
print_alphabet_pyramid(rows)
