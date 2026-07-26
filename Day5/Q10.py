# Take an integer (1–9999) and check if the sum of its digits is greater than the product
# of its digits.


num = int(input("Enter a number (1-9999): "))

temp = num
sum = 0
product = 1

while temp > 0:
    digit = temp % 10
    sum = sum + digit
    product = product * digit
    temp = temp // 10

print("Sum of digits =", sum)
print("Product of digits =", product)

if sum > product:
    print("Sum is greater than Product")
else:
    print("Sum is not greater than Product")