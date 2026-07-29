# Find the difference between the largest and smallest element.

arr = [100,99,88,77,66,55,44,33,22,11]

kk = arr[0]

for i in arr:
    if i>kk:
        kk=i

print("largest Element.")
print(kk)

for i in arr:
    if i <kk:
        pp = i

print("Smallest Element.")
print(pp)

print("Between Of The largest and Smallest Element =",kk -pp)