# . Print all unique elements (those that occur exactly once).
arr = [1, 2, 2, 3, 1, 4, 5]

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count == 1:
        print(arr[i])