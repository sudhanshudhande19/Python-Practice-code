# Take three numbers and check if they are in arithmetic progression.
num1 = int(input("enter the number ="))
num2 = int(input("enter the number ="))
num3 = int(input("enter the number ="))

sum  = num2 - num1
sum2 = num3 -num2

if sum == sum2:
    print("Arithtic progession")
else:
    print("not arithic progession")