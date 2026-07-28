# Find the average of array elements.
n = int(input("Enter The Number ="))

arr =[]

for i in range(n):
    num = int(input("Enter the Array Element ="))
    arr.append(num)

sum = 0

for j in arr:
    sum =  sum +j

print("Average Of Array Elements =",sum/len(arr))