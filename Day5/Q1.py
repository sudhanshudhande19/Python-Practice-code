# Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the
# origin.
x =  int(input("enter the x axis ="))
y = int(input("enter the y axis ="))

if x == 0 and y == 0:
    print("Origin")
elif y == 0:
    print("Point lies on X-axis")
elif x == 0:
    print("Point lies on Y-axis")
else:
    print("Point does not lie on X-axis or Y-axis")
