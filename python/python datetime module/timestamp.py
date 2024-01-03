from datetime import datetime

# Input: Unix timestamp
#timestamp = 1641043845.0
ct=datetime.now()
print("Current time:",ct)
ts=ct.timestamp()
print("Timestamp:",ts)


# Convert timestamp to datetime
converted_datetime = datetime.fromtimestamp(ts)

# Print the result
#print("Timestamp:", timestamp)
print("Datetime:", converted_datetime)
