#Initialize the empty list at the beginning:
nums = []
while True:
    try:
        #All inputs are strings, so the digit string must be converted to an int.
        digit = int(input("Please enter your phone number, one digit at a time. "))
    except ValueError:
        print("That is not a valid digit.  Please try again.")
        continue
    if nums == "":
        print("You pressed enter without entering your digits.  Please try again.")
    if digit < 0:
        print("You must enter a positive number")
    if digit > 9:
        continue
    #Add the digits to a list, so you can use list indexing later to insert the parentheses at a certain pos.
    nums.append(digit)


    print("Your number(s) so far are: ", nums)
    print("You've entered ", len(nums), "number(s)")
    #If the length of the list of numbers is 10 numbers long, the number is ready for formatting:
    if len(nums) == 10:
        print("You've now entered a complete phone number!")
        nums.insert(0, "(")
        nums.insert(4, ")")
        nums.insert(8, "-")
    #Items in a list are separated by commas. When the number is ready, we don't want that.
    #We use join to join all numbers in the list together again.  Then str to convert all to strings.
        phoneNumber = "".join(map(str, nums))
        print("Your telephone number is: ", phoneNumber)
        break







