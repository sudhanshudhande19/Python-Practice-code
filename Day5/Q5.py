# Take a 3-digit number and check if the sum of the first and last digit equals the middle
# digit.
num = [2,4,2]

total  = num[0] + num[2]
if num[0] + num[2] == num[1]:
    print("middle number is equal of sum first and last digit")
else:
    print("middle number are NOT equal of sum first and last digit")