# Find the index of the minimum element.
arr = [55, 99, 88, 6, 778, 545, 364]

mainimum = arr[0]

for i in arr:
    if i   <  mainimum:
        mainimum = i
arr.append(mainimum)
print("Mainimum Element Index is", arr.index(mainimum))