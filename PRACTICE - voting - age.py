
name = input("What is your name? ")
print("Hello,", name)
while True:
    try:
        age = int(input('How old are you?'))
        if age > 18:
            print("You are old enough to vote")
            break
        else:
            print("I'm sorry,", name, ", but you are not of legal voting age.", "You are only", str(age))
            print("Please come back in", int(18 - age), "years, and then you can vote.")
            break
    except ValueError:
        print("That is not a valid age.  Please enter again.")


