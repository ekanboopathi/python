class Bank:
    def __init__ (self):
        self.account_no = 20987654
        self.name = "BOOPATHI"
        self.balance = 23450986

    def deposite(self):
        amount=int(input("Enter the Deposite amount:"))
        self.balance+=amount
        print("Your balance amount:",self.balance)

    def withdrawal(self):
        withdrawal=int(input("Enter the Withdrawal amount:"))
        if self.balance >= withdrawal:
            self.balance-=withdrawal
            print("withdrawal amount",withdrawal)
            print("Your balance amount:",self.balance)
        else:
            print("Amount not Sufficient")

b=Bank()
m=input("Deposite or Withdrawal:")
if m =="Deposite":
    b.deposite()
elif m=="Withdrawal":
    b.withdrawal()
else:
    print("Sorry it is invalid input")
