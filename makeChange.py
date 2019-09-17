import math
"""pandas is the 1st ever successfully installed module, where I had to install it first
in PyCharm, and then here. And it actually worked! I had TRIED to manually install
Beautiful Soup for a web scraping program, but the install failed.  THIS time it 
WORKED!! Yay!! I rock!!"""
import pandas as pd

hundred = 100.00
fifty = 50.00
twenty = 20.00
ten = 10.00
five = 5.00
one = 1.00
nickel = .05
pennies = .01
quarter = .25
dime = .10


#All inputs are in string format, so the inputs have to be converted to a float.
while True:
    try:
        cost = float(input("What is the cost? "))
        break
    except ValueError:
        print("Error occurred. Please enter only number amounts. Please try again.")


while True:
    try:
        amountTendered = float(input("What is the amount tendered? "))
        print("\n")
        changeDue = amountTendered - cost
        if amountTendered < cost:
            print("Your item costs: ", cost, "You have given me only: ", amountTendered)
            print("You still owe: ", (cost - amountTendered))
        else:
            break
    except ValueError:
        print("Error occurred. Please enter only number amounts. Please try again.")

#This is my 1st ever DataFrame!! Yay!
df = pd.DataFrame([amountTendered, cost, changeDue],
                  index=['Amount Tendered:', 'Minus Cost:', 'Total Change Due:'],

                  columns=['Amounts:'])
print(df)

print("*" * 30)
print("\n")
print("*" * 30)
print("The breakdown of bills is as follows: ")
print("*" * 30)
if changeDue >= hundred:
    # All division results in a float(decimal format).
    num100s = changeDue // hundred
    print("100's x {}".format(num100s))
    #The -= is the same as saying, "changeDue = changeDue - (num100's * hundred")
    changeDue -= (num100s * hundred)
elif changeDue < hundred:
    print("")

if changeDue >= fifty:
    num50s = (changeDue % hundred) // fifty
    print("50's x {}".format(num50s))
    changeDue -= (num50s * fifty)
elif changeDue < fifty:
    print("")

if changeDue >= twenty:
    num20s = (changeDue % hundred % fifty) // twenty
    print("20's x {}".format(num20s))
    changeDue -= (num20s * twenty)
elif changeDue < twenty:
    print("")

if changeDue >= ten:
    num10s = (changeDue % hundred % fifty % twenty) // ten
    print("10's x {}".format(num10s))
    changeDue -= (num10s * ten)
elif changeDue < ten:
    print("")

if changeDue >= five:
    num5s = (changeDue % hundred % fifty % twenty % ten) // five
    print("5's x {}".format(num5s))
    changeDue -= (num5s * five)
elif changeDue < five:
    print("")

if changeDue >= one:
    num1s = (changeDue % hundred % fifty % twenty % ten % five) // one
    print("1's x {}".format(num1s))
    changeDue -= (num1s * one)
elif changeDue < one:
    print("")

print("*" * 30)
print("The change due in coin is: ", round(changeDue, 2))
print("The coin breakdown is as follows:")
print("*" * 30)

if changeDue >= quarter:
    num25s = (changeDue % hundred % fifty % twenty % ten % five % one) // quarter
    print("Quarters x {}".format(num25s))
    changeDue -= (num25s * quarter)
    # The 2 rounds the number to 2 decimal places.
    changeDue = round(changeDue, 2)
elif changeDue < quarter:
    print("")

if changeDue >= dime:
    numDimes = (changeDue % hundred % fifty % twenty % ten % five % one % quarter) // dime
    print("Dimes x {}".format(numDimes))
    changeDue -= (numDimes * dime)
    changeDue = round(changeDue, 2)
elif changeDue < dime:
    print("")

if changeDue >= nickel:
    numNickels = (changeDue % hundred % fifty % twenty % ten % five % one % quarter % dime) // nickel
    print("Nickels x {}".format(numNickels))
    changeDue -= (numNickels * nickel)
    changeDue = round(changeDue, 2)

if changeDue >= pennies:
    changeDue = round(changeDue, 2)
    numPennies = (changeDue % hundred % fifty % twenty % ten % five % one % quarter % dime % nickel) / pennies
    print("Pennies x {}".format(numPennies))
    changeDue -= (numPennies * pennies)

if changeDue < .01:
    print("*" * 30)
    print("All change due has been given")
    print("*" * 30)
else:
    print("Customer still due {}".format(round(changeDue, 2)))



