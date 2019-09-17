import re

while True:
    password = input("Please enter a password containing at least 6-12 characters, \n "
                     "one number, one UPPERCASE letter, and one special character. ")

    pattern = r"^(?=.*[A-Z])(?=.*[A-Za-z])(?=.*[0-9])(?=.*[^a-zA-Z0-9]).{6,12}$"

    if not re.search(pattern, password):
        print("*" * 35)
        print("Your password is invalid.")
        print("*" * 35)
    else:
        print("*" * 35)
        print("Your new password is: ", password)
        break

    if not re.search("^.{6,12}$", password):
        print("Your password is not between 6-12 characters.  Your password is", "\n",
              len(password), "characters long")
        print("*" * 35)

    if not re.search("[A-Z]", password):
        print("Your password needs at least one UPPERcase letter")
        print("*" * 35)

    if not re.search("[\d]", password):
        print("Your password needs at least one digit")
        print("*" * 35)

    if not re.search("[^\w]", password):
        print("Your password needs at least one special character")
        print("*" * 35)



