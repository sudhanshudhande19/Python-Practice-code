# ake time (hours and minutes) and print the smaller angle between the hour and
# minute hands.

time  = int(input("enter the time ="))
minutes = int(input("enter tyhe minutes ="))
total = time * 30
total1 = minutes * 6
total2 = total - total1
print("big angle is ", total2)
print("samller angle is",360 - total2)