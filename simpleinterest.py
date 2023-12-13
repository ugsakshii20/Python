def calculate_simple_interest(principal, rate, time):
  """
  This function calculates the simple interest based on principal, rate, and time.
  """
  simple_interest = (principal * rate * time) / 100
  return simple_interest

# Get user input
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (%): "))
time = float(input("Enter time (years): "))

# Calculate and print simple interest
simple_interest = calculate_simple_interest(principal, rate, time)
print(f"Simple Interest: {simple_interest}")
