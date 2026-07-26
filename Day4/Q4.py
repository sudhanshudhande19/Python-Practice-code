# Take income and age, and check if eligible for tax (age > 18 and income > 5 L)
age = int(input("enter the age = "))
income = int(input("enter the incone = "))
if age  >= 18  and income >= 500000:
    print("eligible of tax")
elif age  <= 18  and income <= 500000:
    print("not eligible of tax")
else:
    print("invalid ")