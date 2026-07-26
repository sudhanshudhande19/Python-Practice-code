# Take three numbers and check if they can form a Pythagorean triplet.

num = int(input("enter the number ="))
num2 =int(input("enter the number ="))
num3 =int(input("enter the number ="))
sum =((num * num) + (num2 * num2))
sum2 =num3 *num3

if sum2 ==sum:
    print("pythagorean triple")
else:
    print("do not pythagorean triple")