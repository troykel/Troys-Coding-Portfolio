import pandas as pd

while True:
    try:
        subTotal = float(input("What is the amount of your bill? "))
    except ValueError:
        print("I did not understand that.  Please try again.")
    else:
        break
while True:
    try:
        tipRate = float(input("What percentage is your tip amount? "))
        tipRate = tipRate / 100
    except ValueError:
        print("No need to include the % symbol")
    else:
        break
while True:
    try:
        taxRate = float(input("What is the local tax percentage? "))
        taxRate = taxRate / 100
    except ValueError:
        print("Don't include the % symbol")
    else:
        break

print("*" * 30)


def tip(billAmount, tipAmount):
    print("The TOTAL Tip amount for a ", tipRate, "% tip, = $", round(subTotal * tipRate, 2))


def totalIncludingTip(subTotal, taxRate, totalTip):
    #print("The TOTAL bill amount, INCLUDING TAX, for a ", tipRate, "% tip is $",
          #round(subTotal * (1 + taxRate) + totalTip, 2))


    df = pd.DataFrame([subTotal, totalTip, totalTax],
    index=['Subtotal:', 'Tip:', 'Tax:'],

    columns = ["TOTALS:"])

    #To add the billTOTAL row with a column total.
    """If there were multiple columns and we wanted to add a total column which is the sum across rows,
    we would use: df['Total'] = df.sum(axis=1)"""

    df.loc['BillTOTAL'] = df.sum()
    print(df)




print("The SUBtotal or Bill Amount without tax and tip = ", subTotal)
print("*" * 30)
print("The tip percentage = ", tipRate)
print("*" * 30)

totalTip = round(subTotal * tipRate, 2)

tip(subTotal, tipRate)
print("*" * 30)

print("The local tax rate = ", taxRate)
totalTax = round(subTotal * taxRate, 2)
print("The TOTAL TAX = $", round(subTotal * taxRate, 2))
print("*" * 30)
totalIncludingTip(subTotal, taxRate, totalTip)


