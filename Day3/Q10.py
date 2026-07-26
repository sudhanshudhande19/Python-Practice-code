#Check whether a number is a perfect square (without using the square root function)
num = int(input("Enter a number: "))
i = 1
while i * i <= num:
    if i * i == num:
        print("Perfect Square")
        break
    i = i + 1
else:
    print("Not a Perfect Square")