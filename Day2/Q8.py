# Take two numbers and determine whether both are even, both are odd, or one is
# even and one is odd.
number = int(input("enter the number = "))
number2 = int(input("enter the 2 number = "))
if  number %2 ==0 and number2 %2 ==0:
            print("Both are Even ")
elif number %2 ==1 and number2 %2 ==1:
        print("Both are Odd")
else:
    print(" Both are not equal even and odd there are different number")