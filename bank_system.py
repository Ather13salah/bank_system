from User import *

users = []

# Bank System  
"""1-create account included 
1- Take Name 
2- take a account number 
3- enter password
2- withdraw
3- Deposit
"""

print ("Welcome!\nLet's create a account.")
print("-"*30)
#Take three inputs from user
users.append(User())
underLine()
#-----------------------------This function to show informations of user---------------------------------------------------
def showInfo():
    for user in users:
        print(f'Your Name is {user.userName.title()}\nAccount Number {user.accountNum}\nPassword {user.passw}')  
#------------------------------------This function to transfer money --------------------------------------------
def transfer():
    for i in  range(1,len(users)):
        print(f"{i}-{users[i].userName}")
    choice = input("Enter your choice to transfer(enter Name): ")
    while  choice not in users[i].userName:
        print("invald choice")
        choice = input("Enter your choice to transfer(enter Name): ")  
    else:
        users[i].deposit()
        print("The transfer money sucessfully")  
        askUser()
#--------------------------------------------------------------------------------
# Message
message = """1-Deposit Money
2-Withdraw Money
3-Add account
4-Transfer
5-Show information
6-Sign out
7-Quit"""
def main():
    while True:
        print(message)#print message for user   
        choice = input("Enter your choice: ")
        if choice =="1":
            users[0].deposit()    
            underLine() 
            askUser()
            underLine()
        elif choice == "2":
            users[0].withdraw()            
            askUser()
            underLine()
        elif choice =="3":
            users.append(User())
            underLine()
        elif choice =="4":
            transfer()  
            underLine()
        elif choice == "5":
            showInfo()    
        elif choice =="6":
            signOut(users) 
            underLine()
            main()
        elif choice == "7":
            print("Thank you! for using this System")
            break


if __name__=="__main__":
    main()        