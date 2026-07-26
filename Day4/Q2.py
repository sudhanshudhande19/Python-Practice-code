# Take three numbers and print the median value (neither maximum nor minimum).
num = [63,34,34]
print(num[1])
if num[1] > num[0] and num[1] > num[2]:
    print("maximum",num[1])
elif num[1] < num[0] and num[1] < num[2]:
    print("minimum", num[1])
else:
    print("neither same ",num[1])