account={
    "name":"",
    "balance":0,
    "history":[]
}

def create_account():
    account["name"]=input("Enter your name:")
    account["balance"]=int(input("Enter the balance:"))
    account["history"].append("Account open with" + str(account["balance"]))
    print("Account created for ", account["name"])

def deposite():
    amount=int(input("Enter the amount to deposite:"))
    if amount <=0:
        print("Amount must be more than zero.")
    else:
        account["balance"]=account["balance"]+amount
        account["history"].append("Deposite"+str(amount))


def withdraw():
    amount=int(input("Enter the amount to withdraw:"))
    if amount <=0:
        print("Withdraw the amount more than 0.")
    elif amount> account["balance"]:
        print(f" your balance is { account["balance"]} please withdraw the amount less than balance")
    else:
         account["balance"]= account["balance"]-amount
         account["history"].append("Withdraw"+ str(amount))
         print("Withdraw Succesful...... The Balance is :",account["balance"])

def check_balance():
    print("Balance :",account["balance"])


def show_history():
    print("------Transaction History-----")
    for item in account["history"]:
        print("-", item)


create_account()


while True:
    print("\n1.Deposit")
    print("2.withdraw")
    print("3.check balance")
    print("4.Transaction History")
    print("5.Exit")

    print()
    choice=int(input("Choose(1-5):"))

    if choice==1:
        deposite()
    elif choice==2:
        withdraw()
    elif choice==3:
        check_balance()
    elif choice==4:
        show_history()
    elif choice==5:
        print("Thank you,",account["name"])
        break
    else:
        print("Invalid Choice, Try again.")
        
        





    
