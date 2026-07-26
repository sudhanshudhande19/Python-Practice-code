# Check if a number is a palindrome.
num = list(input("enter the number  ="))
tem =list(num)
tem.reverse()
if num == tem:
    print("is  palindrome ")
else:
    print("is not palindrome")