# Print the table of a given number (n × 1 to n × 10).
n= int(input("enter the number ="))
for i in range(1,11):
    sum = n * i
    print(n,"*",i,"=",sum)