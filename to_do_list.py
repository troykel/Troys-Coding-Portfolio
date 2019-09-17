import re

name = input("What is your name? ")
print(name + "\'s To-Do-List")

"""The various items in the to-do list are added, one-by-one, into a list (mylist)"""
mylist = []
count = 1
while True:
    newitem = input("What do you want to add to your to-do-list?")
    """Type 'remove' at prompt to remove the last item entered.  
    Type 'nothing' to quit the program and compile your list."""

    if newitem == "":
        print("You didn't respond.")
        done_or_not = input("Are you done with your list?")

        if done_or_not == "yes" or done_or_not == "YES":
            print("\n")
            print("Your to-do-list is complete")
            print("You have " + str(count - 1) + " items on your to-do-list: \n")
            # lists each count eg 1: First item in list. 2: Second item in list and so on.
            for count, item in enumerate(mylist, start=1):
                print("{}: {}".format(count, item))
            break
        else:
            continue

    """The RE, as written below, will match(allow) (sample), but not ( or ) by themselves. 
    It will match *sample or sample*, but not * by itself. It will match(allow) make $, 
    but not $ by itself. It will match dog & cat, but not & by itself, etc"""

    if not re.match("[(*]?[\d\w]+[$&@*)%/+_.]*", newitem):
        print("Sorry, I do not understand that.  Please try again.")
        continue


    char_count = 0
    for char in newitem:
        char_count += 1
    if len(newitem) > 100:
        print("Your entry is", char_count, "characters long.")
        print("There is a 100 character limit to each to-do item.")
        continue

    if newitem == "nothing" or newitem == "NOTHING" or newitem == "Nothing":
        print("\n ")
        print("Your to-do-list is complete!")
        print("You have " + str(count - 1) + " items on your to-do-list: \n")
        # lists each count eg 1: First item in list. 2: Second item in list and so on.
        for count, item in enumerate(mylist, start=1):
            #Print the count, followed by : then the item itself.
            print("{}: {}".format(count, item))
        break

    if newitem == "remove" or newitem == "REMOVE" or newitem == "Remove":
        print("Let's remove the last item")
        count -= 1
        # The pop method removes the last list item
        mylist.pop()
        continue

    print(str(count) + ": " + newitem)
    mylist.append(newitem)
    count += 1
