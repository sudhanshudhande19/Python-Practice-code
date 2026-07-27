# Check if a number is a strong number (sum of factorials of digits = number).
number = int(input("Enter a number: "))

temp = number
sum = 0

while number > 0:
    digit = number % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial = factorial * i

    sum = sum + factorial
    number = number // 10

if sum == temp:
    print(temp, "is a Strong Number")
else:
    print(temp, "is Not a Strong Number")