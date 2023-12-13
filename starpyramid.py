def print_star_pyramid(rows):
  """
  This function prints a star pyramid pattern with the given number of rows.
  """
  for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
      print(" ", end="")
    # Print stars
    for j in range(i):
      print("*", end="")
    print()

# Define the number of rows
rows = 5

# Print the pyramid
print_star_pyramid(rows)
