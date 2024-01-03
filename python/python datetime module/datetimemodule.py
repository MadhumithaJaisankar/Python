from datetime import datetime

# Current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# Formatting datetime using strftime
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M")
print("Formatted Datetime:", formatted_datetime)

# Parsing a string to datetime using strptime
date_string = "03 January 2024"
parsed_datetime = datetime.strptime(date_string, "%d %B %Y")
print("Parsed Datetime:", parsed_datetime)
