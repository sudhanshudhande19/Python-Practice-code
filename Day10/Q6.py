# Find the sum of all elements except the largest and smallest.
arr = [100, 99, 88, 77, 66, 55, 44, 33, 111, 11]

largest = arr[0]
smallest = arr[0]
total = 0

for i in arr:
    total += i

    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

result = total - largest - smallest

print("Sum except largest and smallest =", result)