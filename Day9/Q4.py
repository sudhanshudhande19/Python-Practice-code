# Find the maximum element in an array.

arr = [55, 99, 88, 66, 778, 545, 364]

maximum = arr[0]

for i in arr:
    if i > maximum:
        maximum = i

print("Maximum Element is", maximum)