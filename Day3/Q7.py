# Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.
amount = int(input("enter the amount ="))
temp = amount

temp = temp % 2000
temp = temp % 500
temp = temp % 100
if temp == 0:
    print("Amount can be evenly divided into 2000, 500 and 100 notes.")
else:
    print("Amount cannot be evenly divided.")