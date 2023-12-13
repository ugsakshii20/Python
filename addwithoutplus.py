def add_without_plus(x, y):
  """
  This function adds two numbers without using the '+' operator.
  """
  carry = 0
  while y:
    carry = (x & y) << 1
    x = x ^ y
    y = carry
  return x

# Get user input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Calculate and print the sum
sum = add_without_plus(x, y)
print(f"The sum of {x} and {y} without using '+' is: {sum}")
