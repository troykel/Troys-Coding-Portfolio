import re

nbr = input("Enter a phone number (11 digits)\n" 
            " with just the numbers: ")

"""REGEX EXPLAINED:
 matches zero or more first digits as either 1, 8, or 9 
followed by (?=) 3 digits, and then 7 digits"""

regex = r"(1|8|9)*(?=\d{3}\d{7})"

if re.search(regex, nbr):
    print("Valid")
else:
    print("Invalid")