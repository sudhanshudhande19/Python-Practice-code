# Take three sides and check if they form a valid triangle.
side  = int(input("enter the 1st side ="))
side2 = int(input("enter the 2nd side ="))
side3 = int(input("enter the 3rd side ="))

if side + side2  > side3 or side + side3 > side2 or side2 + side3 > side:
    print("this is valid tringle ")
else:
    print("this is not valid tringle")