# Take a month number (1–12) and print the number of days in that month (ignore leap
# years).
month  = int(input("enter the month number ="))
if month == 1:
    print(month,"January: 31 days")
elif month == 2:
    print(month,"February: 28 days (29 in a leap year)")
elif month == 3:
    print(month,"March: 31 days")
elif month == 4:
    print(month,"April: 30 days")
elif month == 5:
    print(month,"May: 31 days")
elif month == 6:
    print(month,"jun:30 day")
elif month == 7:
    print(month,"july : 31 day")
elif month == 8:
    print(month,"August: 31 days")
elif month == 9:
    print(month,"September: 30 days")
elif month == 10:
    print(month,"October: 31 days")
elif month == 11:
    print(month,"November: 30 days")
else:
    print(month,"December: 31 days")
