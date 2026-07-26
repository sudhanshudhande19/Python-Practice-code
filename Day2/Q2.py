# Check if one of two given numbers is a multiple of the other.
num = int(input("ente the number  ="))
num2 = int(input("enter the number = "))
if  num % num2 == 0 or num2 % num ==0:
   print("One number is a multiple of the other.")
else:
    print("Neither number is a multiple of the other.")