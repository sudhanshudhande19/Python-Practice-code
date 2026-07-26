# Take a character and check if it is a letter, a digit, or neither.
check =(input("enter the character = "))
if 'a' <= check <= 'z' or 'A' <= check <= 'Z':
    print("this is letter")
elif '1' <= check <= '9':
    print("this is digit")  
else:
    print("neither")   
