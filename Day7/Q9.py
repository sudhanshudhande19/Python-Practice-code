# 8. Check if a number is prime or not.
num = int(input("Enter the number = "))

prime = True

if num <= 1:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

if prime:
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")
