
for i in range(500):
    result = i**3
    #If less than 10, it's a 1 digit number
    if i < 10:
        #Convert the result variable to a string, so it can be indexed / sliced
        #Convert it back to an integer, so it can be compared to i, which is an integer.
        """[-1:] slices the resulting string, starting from 1 character BACKwards, hence
        -1, from the end of the string, to the END of the string, which is why there's
        nothing after the colon: symbol.  When result is a 2 digit number(string), that has
        to be increased to -2, or starting 2 characters backwards from the end, to the end.
        When result is a 3 digit number(string), that has to be increased to -3, or 3 
        characters backwards from the end, to the end, etc."""
        if int(str(result)[-1:]) == i:
            print("{} is a Trimorphic Number:".format(i))
            print("{}**3 = {}".format(i, result))
    #If statement checks if it's a 2 digit number
    if (i > 9) and (i < 100):
        #Is the sliced section of the result variable == i??
        if int(str(result)[-2:]) == i:
            #If it is, print out the following:
            print("{} is a Trimorphic Number:".format(i))
            print("{}**3 = {}".format(i, result))
    #If statement checks if it's a 3 digit number
    if (i >= 100) and (i < 1000):
        if int(str(result)[-3:]) == i:
            print("{} is a Trimorphic Number:".format(i))
            print("{}**3 = {}".format(i, result))

