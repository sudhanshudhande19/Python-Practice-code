# Take a 3-digit number and determine if the middle digit is the largest, smallest, or
# neither
arr = [2,9,6]
if arr[1] > arr[0] and arr[1] > arr[2]:
    print("middle number is largest number ",arr[1])
elif arr[1] < arr[0] and arr[1] < arr[2]:
    print("middle number is smallest number ",arr[1])
else:
    print("middle number is neither number ")