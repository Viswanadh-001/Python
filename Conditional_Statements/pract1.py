#find the greatest of 3 numbers given by the user

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if a >= b and a >= c:
    print("first number is greatest")
elif b >= c:
    print("Second number is greatest")
else:
    print("Third number is greatest")