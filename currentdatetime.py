import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Print the current date and time
print(f"Current date and time: {current_datetime}")

# Print the current date and time in specific format
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date and time: {formatted_datetime}
