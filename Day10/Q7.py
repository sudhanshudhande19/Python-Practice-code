# Count how many pairs of elements have a sum equal to a given number k.
arr = [1, 2, 3, 4, 5, 6, 7]
k = 10

count = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == k:
            count += 1

print("Number of pairs =", count)