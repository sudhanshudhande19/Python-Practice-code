# Find the second largest element in an array.
arr = [100, 99, 88, 77, 66, 55, 44, 33, 111, 11]
kk=  arr[0]
for i in arr:
    if i>kk:
        kk=i
print(arr)
print("Check The Largest element Of In Array")
print(kk)