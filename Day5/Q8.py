# Take two dates (day and month) and determine which one comes first in the
# calenda
day1 = int(input("Enter first day: "))
month1 = int(input("Enter first month: "))

day2 = int(input("Enter second day: "))
month2 = int(input("Enter second month: "))

if month1 < month2:
    print("First date comes first")
elif month1 > month2:
    print("Second date comes first")
else:
    if day1 < day2:
        print("First date comes first")
    elif day1 > day2:
        print("Second date comes first")
    else:
        print("Both dates are the same")