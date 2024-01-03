import re

pattern = re.compile(r'\d{4}-\d{4}-\d{4}')

aadharno = '1234-5678-9101'
if pattern.match(aadharno):
    print("Valid Aadhar number")
else:
    print("Invalid Aadhar number")
