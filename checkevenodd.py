def check_odd_even(number):
  """
  This function checks if a number is odd or even.
  """
  if number % 2 == 0:
    print(f"{number} is even.")
  else:
    print(f"{number} is odd.")

# Get user input
number = int(input("Enter a number: "))

# Check odd or even
check_odd_even(number)
