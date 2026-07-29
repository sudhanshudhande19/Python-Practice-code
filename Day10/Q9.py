# Print the frequency of each distinct element.
arr = [1, 2, 2, 3, 1, 4, 2]

for i in range(len(arr)):
    count = 1

    if arr[i] == -1:
        continue

    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            count += 1
            arr[j] = -1

    print(arr[i], "->", count)