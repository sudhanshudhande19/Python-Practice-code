# Take n elements and print only those greater than a given value k.
n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

k = int(input("Enter the value of k: "))

print("Elements greater than", k, "are:")

for i in arr:
    if i > k:
        print(i)