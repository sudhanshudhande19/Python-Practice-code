# Check whether a given integer is single-digit, double-digit, or multi-digit
number = int(input("enter the number= "))
if number <= 9:
    print("this is single- digit")
elif number <= 99:
    print("this is double -digit")
elif number < 1000:
    print("multi-digit ")
else:
    print("nono")