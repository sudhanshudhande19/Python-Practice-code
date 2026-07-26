# Take two numbers and check if both are positive and their sum is less than 100.
num  = int(input("enter the number = "))
num2 = int(input("enter the number = "))
if num and num2 >=0:
    print("positive")
else:
    print("negetive")
if num +  num2 <= 100:
    print("less then 100")
else:
    print("not less the 100")