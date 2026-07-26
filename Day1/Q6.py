# Take three numbers and print the largest.
num1  = int(input())
num2= int(input())
num3 = int(input())
if num1 > num2 :
  if num1 > num3:
    print("num1 is largest number =" ,num1)
  else:
    print("num3 is largest nuber =",num3)
elif num2 > num3:
  print("num2 is largest number =",num2)
else:
  print("num3 is largest number =", num3)