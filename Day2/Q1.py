# Take marks (0–100) and print the corresponding grade (A/B/C/D/F).
name  = input("ente the name = ")
marks = int(input("enter the marks ="))
if 90 < marks  <=100:
    print("Grade A")
elif 80 < marks <= 90:
    print("Grade B")
elif 60 < marks <= 80:
    print("Grade C")
elif 35 <= marks <=60:
    print("Grade D")
else:
    print("Grade F")



