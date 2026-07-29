# Find the second smallest element in an array
arr = [100,99,88,77,66,55,44,33,22,11]

kk = arr[0]

for i in arr:
    if i < kk:
        kk = i
print(arr)
print("Check The Smallest element Of In Array")
print(kk)