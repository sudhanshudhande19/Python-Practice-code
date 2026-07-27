#  Print first n terms of a geometric progression (a, r).
a = int(input("Enter first term: "))
r = int(input("Enter common ratio: "))
n = int(input("Enter number of terms: "))

term = a

for i in range(n):
    print(term, end=" ")
    term = term * r