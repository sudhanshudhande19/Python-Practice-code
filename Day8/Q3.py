# Print all numbers between a and b divisible by 7
number  = int(input("enter the number  = "))
number2 = int(input("enter the number  = "))

for i in range(number, number2+1):
    if i %7 ==0:
        print(i)