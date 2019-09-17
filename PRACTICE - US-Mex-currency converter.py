pesosPerDollarRate = 18.79

US_Dollars = float(input("How many dollars do you have? "))
MexPesos = US_Dollars * pesosPerDollarRate
#Rounding MexPesos to 2 decimal places
print("In Mexican Pesos, that would be: ", "Mex$", round(MexPesos, 2))

print("=" * 50)

dollarsPerPesoRate = .053
#All inputs are in string format, which must be converted to a float.
mexPesos = float(input("How many pesos do you have? "))
dollars = mexPesos * dollarsPerPesoRate
#Rounding dollars to 2 decimal places
print("In dollars, that would be: ", "$", round(dollars, 2))


