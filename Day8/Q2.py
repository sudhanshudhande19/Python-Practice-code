# Print cubes of numbers from 1 to n.
number  = int(input("enter the number = "))
for i in range(1,number+1):
    sum = i**3
    print(f"{i}*{3}={sum}")