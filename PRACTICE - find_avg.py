count = 0
total = 0
mylist = []
options = ["quit", "Quit", "QUIT", "QUit"]
while True:
    num = input("What is your number? (Or type 'quit') ")
    try:
        mylist.append(int(num))
    except ValueError:
        if num in options:
            break
    count += 1
    for num in mylist:
        print(num, "|", end="")

    total += int(num)
    print("\nSum = ", total)
    print("Count = ", count)
    print("Average = ", round(total / count, 2))
    if count == 20:
        break
