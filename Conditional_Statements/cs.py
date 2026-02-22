# Grade students based on marks by getting marks input by the user
# marks >= 90, grade =“A”
# 90 > marks >= 80, grade =“B”
# 80 > marks >= 70, grade =“C”
# 70 > marks, grade =“D”

marks = float(input("Enter the marks: "))

if marks >= 90:
    print("Grade = A")
elif marks >= 80 and marks < 90:
    print("Grsde = B")
elif marks >= 70 and marks < 80:
    print("Grade : C")
else:
    print("Grade : D")