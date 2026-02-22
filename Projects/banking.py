#display initial balance to user 

initialBalance = 10000.0000 
print("Current Balance:",initialBalance)
# take input from user regarding operation he wants to perform
ops = input("Enter Operation:")
#Operations are: add, Withdraw, View
# if user selects add ask user for input of adding amount and add the input to initial balance 
# if user selects withdraw ask user for input of withdraw amount and delete the input to initial balance
# if user dosnt delect any of above display balace

if ops == "Add":
    depositAmt= int(input("Add Amount:"))
    initialBalance += depositAmt
    print(initialBalance)
elif ops == "Withdraw":
     withdrawAmount= int(input("Withdraw amount:"))
     initialBalance -= withdrawAmount
     print(initialBalance)         
else :
   print("Current Balance:",initialBalance)    