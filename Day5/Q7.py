# take day and month and check if it forms a valid calendar date (ignoring leap years).
month  = int(input("enter the month = "))
date = int(input("enter the date ="))

if month ==1:
    if 1 <=  date <= 31:
        print("January month valid date ")
elif month ==2:
    if 1 <= date <= 28:
        print("February month valid date ")
elif month == 3:
     if 1 <= date <= 30:
        print("March month valid date ")
elif month == 4:
     if 1 <= date <= 30:
        print("Aprialmonth valid date ")
elif month == 5:
     if 1 <= date <= 30:
        print("May month valid date ")
elif month == 6:
     if 1 <= date <= 31:
        print("June month valid date ")
elif month == 7:
     if 1 <= date <= 30:
        print("Junly month valid date ")
elif month == 8:
     if 1 <= date <= 31:
        print("Aagust month valid date ")
elif month == 9:
     if 1 <= date <= 31:
        print("September month valid date ")
elif month == 10:
     if 1 <= date <= 31:
        print("October month valid date ")
elif month == 11:
     if 1 <= date <= 30:
        print("November month valid date ")
elif month == 12:
     if 1 <= date <= 31:
        print("December month valid date ")
else:
    print("Not valid month and date")
