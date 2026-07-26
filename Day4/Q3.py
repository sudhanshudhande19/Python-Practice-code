# Take 24-hour time (hours and minutes) and print whether it is AM or PM.
time =int(input("enter the time = "))
min = int(input("enter the minutes ="))
if 0 <= time <= 11:
    print(time ,":",min, "AM")
elif 12 <= time <=23:
    print(time ,":",min,"PM")
else:
    print(time ,":",min,"Invalid Time")
