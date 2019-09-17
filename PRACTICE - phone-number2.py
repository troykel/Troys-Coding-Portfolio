import random
#Generating a random sample of 10 numbers and storing it in the variable called number
number = ''.join(random.sample("0123456789", 10))
#Converting the number variable to a list, so that it can be indexed later.
number = list(number)
number.insert(0, "(")
number.insert(4, ")")
number.insert(8, "-")
number[1] = random.randint(2, 9) #To exclude area codes starting with 0 or 1.
number[5] = random.randint(2, 9) #To exclude prefixes that start with 1.
"""List elements are separated by commas, which for a telephone 
number is undesirable, so the following line reunites all the 
elements of the list, without commas."""
phoneNumber = "".join(map(str, number))
print("Your new telephone number is: ", phoneNumber)

