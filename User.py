
class User():
    credit=0
    userName=""
    accountNum=""
    passw=""
    def __init__(self):
        self.userName = input("Enter your Name: ")

        self.accountNum= input("Enter account Number (4 numbers): ")
        while len(self.accountNum) != 4:
            print("invalid Number")
            self.accountNum= input("Enter account Number (4 numbers): ")  

              
        self.passw = input("Enter your password (at least 6 characters): ")
        while len(self.passw)<6:
            print("invalid password")
            self.passw= input("Enter your password (at least 6 characters): ")

    @classmethod
    def displayCredit(self):
        print(f"the account is {self.credit}")       
        
    @classmethod
    def deposit(self):         
        deposit = float(input("Enter money to Deposit (at least 500): "))
        print("-"*30)

        while  deposit<500:
            print('at least 500')
            deposit = int(input("Enter money to Deposit (at least 500): "))
        self.credit+=deposit
        self.displayCredit()
    @classmethod            
    def withdraw(self):
        with_draw = int(input("Enter money to Withdraw (at least 100): "))
        print("-"*30)
        if self.credit:
            while with_draw<100:
                print("at least 100 to Withdraw money")
                with_draw = int(input("Enter money to Withdraw (at least 100): "))

            self.credit-=with_draw
            self.displayCredit()
        else:
            print("Don't withdraw")  
        
def underLine():
    print("-"*30)     
    
def askUser():
    user_ch = input("Do you make any operator(y/n) : ")
    if user_ch.lower() !="y":
        quit()

def signOut(users):
    for user in users:
        users.remove(user)
    print('Thanks you for you')
    quit()