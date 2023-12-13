def print_inverted_pyramid(rows):
  """
  This function prints an inverted pyramid with the given number of rows.
  """
  for i in range(rows, 0, -1):
    for j in range(i):
      print("*", end="")
    print()

# Define the number of rows
rows = 5

# Print the pyramid
print_inverted_pyramid(rows)
