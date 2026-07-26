# . Take a year and print the corresponding century (e.g., “19th century”, “20th century”)
year = int(input("enter the year ="))

if 1801 <= year <= 1900:
    print(" 19th century")
elif 1901 <= year <= 2000:
    print(" 20th century")
elif 2001 <= year <= 3000:
    print(" 21th century")
else:
    print(" not valid year")