# Ask user name
name = input("Enter user name:")

# Display welcome message with user name
print("Welcome:",name)

# Display initial balance (5000)
initial_balance = 5000
print("Initial Balance:",initial_balance)

# Take input from user regarding operation he wants to perform
# Operations are: Deposit, Withdraw, Check

operation = input("Choose the operation (Deposit, Withdraw, Check):")

# If user selects Deposit:
#     Ask user for deposit amount
#     If amount <= 0 → print "Invalid Amount"
#     If amount > 50000 → print "Large Deposit Alert"
#     Add amount to balance
#     Print "Deposit Successful"
#     Display updated balance
if operation == "Deposit":
   deposit_amt = float(input("Enter deposit amount:"))
   if deposit_amt <= 0:
      print("Invalid Amount")
   elif deposit_amt > 50000:
      print("Large Deposit Alert!")
      initial_balance += deposit_amt
      print("Deposit Successful")
      print("Updated Balance:",initial_balance)
   else:
    initial_balance += deposit_amt
    print("Deposit Successful")
    print("Updated Balance:", initial_balance)

# If user selects Withdraw:
#     Ask user for withdrawal amount
#     If amount <= 0 → print "Invalid Amount"
#     If amount > balance → print "Insufficient Balance"
#     If withdrawal is more than 70% of balance → print "High Withdrawal Warning"
#     Deduct amount from balance
#     If balance becomes 0 → print "Account Empty"
#     Print "Withdrawal Successful"
#     Display updated balance
elif operation == "Withdraw":
   with_amt = float(input("Enter withdraw amount:"))

   if with_amt <= 0:
      print("Invalid Amount")
   elif with_amt > initial_balance:
       print("Insufficient Balance")
   else:
    if with_amt >= 0.7 * initial_balance:
        print("High Withdrawal Warning")
        initial_balance -= with_amt
        if initial_balance == 0:
         print("Account Empty")

    print("Withdraw Successfull")
    print("Updated Balance:",initial_balance)


# If user selects Check:
#     Display current balance
elif operation == "Check":
 print("Your Balance is:",initial_balance)

# If user enters anything else:
#     Print "Invalid Operation"
else:
   print("Invalid Operation!!")

# After transaction, display summary:
#     User name
#     Operation performed
#     Remaining balance
print("----- Transaction Summary -----")
print("User Name:", name)
print("Operation:", operation)
print("Remaining Balance:", initial_balance)