num1 = float(input("Enter first number: "))
num2 = float(input("Enter Second number: "))

operations = input("Slect the operations (+, -, *, /): ")

if operations == '+':
   result = num1 + num2
elif operations == '-':
   result = num1 - num2
elif operations == '*':
   result = num1 * num2
elif operations == '/':
   if num2 != 0:
      result = num1 / num2
   else:
       result = "Error division by zero."
else:
   result = "Invalid operation" 
print("Result: ",result)