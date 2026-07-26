#  Print sum of first n terms of Fibonacci series.
n = int(input("Enter the number of terms: "))

a = 0
b = 1
sum = 0

for i in range(n):
    sum = sum + a
    c = a + b
    a = b
    b = c

print("Sum =", sum)