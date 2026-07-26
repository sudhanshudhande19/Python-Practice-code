# Take a password string and check basic rules (length ≥ 8 and contains at least one digit )
password = input("Enter password: ")
digit = False
if len(password) >= 8:
    for ch in password:
        if '0' <= ch <= '9':
            digit = True
            break
    if digit:
        print("Valid Password")
    else:
        print("Invalid Password (No digit found)")
else:
    print("Invalid Password (Length should be at least 8)")