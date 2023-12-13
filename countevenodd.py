def count_even_odd(n):
  """
  This function counts the first n even and odd numbers using list comprehension.
  """
  even_numbers = [i for i in range(2*n) if i % 2 == 0]
  odd_numbers = [i for i in range(2*n) if i % 2 != 0]
  return len(even_numbers), len(odd_numbers)

# Get user input
n = int(input("Enter the number of numbers: "))

# Count and print even and odd numbers
even_count, odd_count = count_even_odd(n)
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
