# Find the index of the maximum element.
arr = [55, 99, 88, 6, 778, 545, 364]

maximum = arr[0]

for i in arr:
    if i   >  maximum:
        maximum = i
arr.append(maximum)
print("Maximum Element Index is", arr.index(maximum))