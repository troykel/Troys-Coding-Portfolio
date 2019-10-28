"""A gapful number is at least a 3 digit number. If
the first and last digits of the number, when joined
together, can be evenly divided into the original number,
then it is a 'gapful number'."""

for i in range(100, 1001):
    num = str(i)
    print("Num is: ", num)
    gap = num[0] + num[-1]
    gap = int(gap)
    print("The gap is: ", gap)
    if i % gap == 0:
        print(i, " is a gapful number!")
        print(i, " is perfectly divisible by: ", gap)
        print("*" * 50)
    else:
        print(i, " is NOT divisible by:", gap)
        print(i, " is NOT a 'gapful number'!")
        print("*" * 50)

