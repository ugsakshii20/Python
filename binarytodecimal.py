def decimal_to_binary(decimal_number):
  """
  This function converts a decimal number to its binary equivalent.
  """
  binary_number = ""
  while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number
    decimal_number //= 2
  return binary_number

def binary_to_decimal(binary_number):
  """
  This function converts a binary number to its decimal equivalent.
  """
  decimal_number = 0
  power = 0
  for digit in binary_number[::-1]:
    decimal_number += int(digit) * 2**power
    power += 1
  return decimal_number

# Get user input
option = input("Enter your choice (1: Decimal to Binary, 2: Binary to Decimal): ")

if option == "1":
  decimal_number = int(input("Enter the decimal number: "))
  binary_number = decimal_to_binary(decimal_number)
  print(f"Binary equivalent: {binary_number}")
elif option == "2":
  binary_number = input("Enter the binary number: ")
  decimal_number = binary_to_decimal(binary_number)
  print(f"Decimal equivalent: {decimal_number}")
else:
  print("Invalid option entered.")

