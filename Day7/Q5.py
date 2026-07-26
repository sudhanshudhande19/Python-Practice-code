# 5. Check if a number is an Armstrong number
num = int(input("Enter a number: "))

count = len(str(num))
sum = 0

for digit in str(num):
    sum = sum + int(digit) ** count

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")