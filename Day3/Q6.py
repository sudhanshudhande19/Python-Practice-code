# Take coordinates (x, y) and determine which quadrant the point lies in.
num1 = int(input("enter the number  ="))
num2 = int(input("enter the number  ="))
if num1 > 0 and num2 > 0:
    print("this is frist quadrant  + +")
elif num1 < 0 and  num2 > 0:
    print("this second quadrant - +")
elif num1 < 0 and num2 < 0 :
    print(" this third quadrant - -")
elif num1 > 0 and num2 <0 :
    print("this is fourth quadrant + -")
else:
    print("not quadrant")