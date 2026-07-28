# Input n and take n integers into an array; print them.

n =int(input("Enter The Number ="))

arr =[]

for i in range(n):
    num = int(input("Enter The Element = "))
    arr.append(num)
    
print("Array Element ")
for j in arr:
    print(j)
