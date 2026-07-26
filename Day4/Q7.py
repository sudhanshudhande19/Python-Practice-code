# Take a weekday number (1–7) and determine if it is a weekday or weekend.
day  = int(input("enter the day number = "))
if 1 <= day <= 5:
    print("weekday")
elif 6 <= day <= 7:
    print("weekend")
else:
    print("invalid day")