# Count how many elements are even and odd
arr = [2,3,4,5,6,7,8,9,10,11,12]

even = 0
odd = 0


for i in arr:
    if i %2== 0:
        even += 1
    elif i %2== 1:
        odd += 1
    

print("Even elements =", even)
print("Odd elements =", odd)
