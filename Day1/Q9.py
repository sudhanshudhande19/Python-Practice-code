# Take a character and check whether it’s uppercase, lowercase, a digit, or a special character
number  = input("enter the chaaracter=")
if number >="A" and number <= "Z":
  print("uppercase")
elif number >="a" and number <= "z":
  print("lowercase")
elif number >="0" and number <= "9":
  print("digit")
else:
  print("special character")