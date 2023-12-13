def find_even_numbers(n):
  """
  This function finds the first n even numbers using list comprehension.
  """
  return [i for i in range(n * 2) if i % 2 == 0]

# Get user input
n = int(input("Enter the number of even numbers: "))

# Find and print even numbers
even_numbers = find_even_numbers(n)
print(f"The first {n} even numbers are: {even_numbers}")
