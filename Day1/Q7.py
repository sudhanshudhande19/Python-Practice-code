#  Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions
temprature = int(input("enter the temprature ="))
if temprature < 0:
  print(temprature,"temprature is colde")
elif temprature >= 0 and  temprature <= 20:
  print(temprature,"temprature is a warn")
elif temprature > 20:
  print(temprature,"temprature is hot")