def reverse_string(text):
  """
  This function reverses the given string using string slicing.
  """
  reversed_string = text[::-1]
  return reversed_string

# Get user input
text = input("Enter the string: ")

# Reverse and print the string
reversed_string = reverse_string(text)
print(f"Reversed string: {reversed_string}")
