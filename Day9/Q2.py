# Find the sum of all elements in an array.
n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

sum = 0

for i in arr:
    sum = sum + i

print("Sum =", sum)

