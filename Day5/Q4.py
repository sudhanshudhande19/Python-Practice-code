# Take three numbers and check if they are in geometric progression.
num1 = int(input("enter the number ="))
num2 = int(input("enter the number ="))
num3 = int(input("enter the number ="))

total = num2 % num1
total1 = num3 % num2
if total == total1:
    print("Geomtice progration")
else:
    print("not geomtice progration")