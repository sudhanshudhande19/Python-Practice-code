# If the sides form a valid triangle, determine whether it is equilateral, isosceles, or
# scalene.
side1 = int(input("enter the 1st side = "))
side2 = int(input("enter the 2nd side = "))
side3 = int(input("enter the 3rd side = "))
if side1  == side2 == side3:
    print("Equliateral tringle ")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("isoscels tringle ")
elif side1 != side2 and side2 != side3 and side3 != side1:
    print("scalen tringle" )
else:
    print("enter the valid side not check this side ")
    