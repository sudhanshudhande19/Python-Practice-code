# Find the sum of all factors of a number
number  = int(input("enter the number  ="))
total  = 0
for i in range(1,number+1):
    if number%i==0:
        total  = total +i
print(total)