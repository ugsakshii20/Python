def print_number_pyramid(rows):
  """
  This function prints a number pyramid pattern with the given number of rows.
  """
  for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
      print(" ", end="")
    # Print numbers
    for j in range(1, i + 1):
      print(j, end="")
    # Print numbers in reverse order
    for j in range(i - 1, 0, -1):
      print(j, end="")
    print()

# Define the number of rows
rows = 5

# Print the pyramid
print_number_pyramid(rows)
