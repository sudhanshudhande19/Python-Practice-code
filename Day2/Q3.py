# Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good
# Evening”, or “Good Night”.
import time
# t = time.strftime('%H :%M : %S')
# hour = int(time.strftime('%H'))
hour = int(input())
if 0 >= hour < 12:
    print("GOOD MORING")
elif 12 >= hour <=17:
    print("GOOD AFTERNOON")
elif 17 <= hour > 0:
    print("GOOD NIGHT")