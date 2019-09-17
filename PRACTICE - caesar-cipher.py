
try:
    original_message = input("Please enter your message ")
except ValueError:
    print("Please enter only letters")

print("Your original message is: '{}'".format(original_message))
print("Your Caesar Cipher is: ")

#Convert the original_message to a list, so it can be indexed.
cipher = list(original_message)

lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

new_letter = 0
newLetter = 0
for letter in cipher:
    if letter in lower_case:
        #Use the index function to find the index of the current letter
        original_letter = lower_case.index(letter)
        try:
            #Add 2 to original_letter to shift the letter 2 places to the right.
            new_letter = lower_case[original_letter + 2]
        #If the letter is at the end of the alphabet, don't add 2 to it's index
        #to avoid IndexErrors.
        except IndexError:
            new_letter = letter
        #Use end="" to avoid printing a newline(so all will be on same line)
        print(new_letter, end="")

    if letter in UPPER_case:
        originalLetter = UPPER_case.index(letter)
        try:
            newLetter = UPPER_case[originalLetter + 2]
        except IndexError:
            newLetter = letter

        print(newLetter, end="")















