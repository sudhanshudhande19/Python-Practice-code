# . Count how many elements are greater than the average of the array

arr = [1, 2, 3, 4, 5, 6, 7]

total = 0
for i in arr:
    total += i

avg = total/len(arr)

for i in arr:
    if i > avg:
        count =+ i

print("Average =", avg)
print("Count =", count)
  