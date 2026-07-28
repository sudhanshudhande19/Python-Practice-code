# Count how many elements are positive, negative, or zero.
arr = [10, -5, 0, 25, -8, 0, 15]

positive = 0
negative = 0
zero = 0

for i in arr:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero += 1

print("Positive elements =", positive)
print("Negative elements =", negative)
print("Zero elements =", zero)