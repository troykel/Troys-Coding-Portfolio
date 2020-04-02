height = 0
rows = 0
cols = 0
count = 0
maxrows = -1
while maxrows < 1 or maxrows > 20:
    try:
        maxrows = int(input("What is the height(maximum number of rows) in your pyramid? "))
        count += 1
        if count >= 1 and maxrows < 1 or maxrows > 20:
            print("Your entry is out of range(1-20).")
    except ValueError:
        print("You must enter an integer(a number) between 1 and 20")


print("The height of your pyramid(maximum number of rows) is: {}".format(maxrows))
#The code below prints the rows for BOTH first and second triangle
for rows in range(1, maxrows + 1):
    #The code below pads the first triangle with spaces before the *'s.
    for spaces in range(maxrows - cols, -1, -1):
        print(end=" ")
    for cols in range(1, rows + 1):
        print("*", end="")
    print(end="  ")
    #The code below prints the columns of the second triangle
    for cols in range(1, rows + 1):
        print("*", end="")
    #The next line prevents all the stars from being printed on the same line.
    print("\n")
