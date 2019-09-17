import random

highest = 100
answer = random.randint(1, highest)

print("Welcome to Troy's number guessing game!  You have a limit of 5 guesses")
print("You can quit anytime by pressing 0")
print("Please guess a number between 1 and {} ".format(highest))
guess = ""

count = 0
while guess != answer:
    try:
        guess = int(input())
    except ValueError:
        print("An error occurred.  Please enter just numbers.")
        continue

    if guess < 0:
        print("Please enter only positive numbers.")
        continue

    if guess < answer:
        if guess == 0:
            print("Thank you for playing!")
            break
        else:
            print("Please guess higher")
            count += 1
            if count == 1:
                print("You have 1 attempt so far!")
            else:
                print("You have {} attempts so far!".format(count))
            if count > 5:
                print("You have exceeded your guess limit.  Game over!")
                break
    if guess > answer:
        print("Please guess lower")
        count += 1
        if count == 1:
            print("You have 1 attempt so far!")
        else:
            print("You have {} attempts so far!".format(count))
        if count > 5:
            print("You have exceeded your guess limit.  Game over!")
            break

else:
    count += 1
    if count == 1:
        print("You guessed correctly in only 1 attempt!")
    if count > 5:
        print("You have {} attempts so far!".format(count))
        print("You have exceeded your guess limit.  Game over!")
    if count > 5 and guess == answer:
        print("OK, you guessed correctly in {} attempts!!  We'll let you slide this ONE time!!".format(count))
    else:
        print("You guessed correctly in only {} attempts!!".format(count))
    print("The number is {}".format(answer))
