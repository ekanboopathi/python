'''
    Advanced OOP 
'''
# USER
class User:
    def __init__(self):
        self.username = 'User'
        self.balance = 500
        self.pin_no = "0000"
        self.acc_no = 38728
class UserManagement(User):
    def __init__(self):
        User.__init__(self)
        self.users = []
    def add_user(self):
        user = User()
        print("Please Add Users below: ")
        user_name = input("Enter your name: ")
        u_balance = input("Enter the minimum balance: ")
        pin = input("Enter the pin number: ")
        acc = input("Enter the acc no: ")
        user.username = user_name
        user.balance = u_balance
        user.pin_no = pin
        user.acc_no = acc
        self.users.append(user)
        return self.users
class ATM():
    # Constructor
    def __init__(self, users_bank):
        self.users_bank = users_bank
    # Method to check balance
    def check_balance(self):
        status = self.check_pin()
        if status != 0:
            for check in self.users_bank:
                if (status == check.pin_no):
                    balance = float(check.balance)
                    check.balance = str(balance)
            print(f"hey {check.username},Your balance is {check.balance}")  
        else:
            print("Incorrect, Please try again!")          
    # Method to check pin number
    def check_pin(self):
        pin_number = input("Enter the pin number: ")
        for pin in self.users_bank:
            # Check the user given pin number equal to defaul pin number
            if pin_number == pin.pin_no:
                return pin_number
            else:
                return 0
    # Method to deposit amount
    def deposit(self):
        status = self.check_pin()
        if status != 0:
            for bal in self.users_bank:
                if(status == bal.pin_no):
                    amount = float(input("Enter the amount to deposit: "))
                    balance = float(bal.balance)  + amount
                    bal.balance = str(balance)
                    print(f"Hey {bal.username}, Your balance is update to {bal.balance}")
        else:
            print("Incorrect PIN, Please try again")
    # Method to withdraw amount
    def withdraw(self):
        status = self.check_pin()
        if status != 0:
            # check the minimum balance to with draw
            for i in self.users_bank:
                if(status == i.pin_no):
                    amount = float(input("Enter the amount to withdraw: "))
                    balance = float(i.balance) - amount
                    i.balance = str(balance)
                    print(f"hey {i.username},Your balance is {i.balance}")  
                else:
                    print("Incorrect PIN, Please try again")
    # Main Execution
user = UserManagement()
users_bank = []
while True:
    command = input("Do you wanna continue (y | n): ")
    if(command == "y"):
        users_bank = user.add_user()
    else: 
        break
# ATM Object initialize
user = ATM(users_bank)
count = 0
while True:
    if(count >= 1):
        atm_opt = input("Do you wanna continue or quit: ")
        if(atm_opt == "continue"):
            option = input("Select any option (Deposit - 0) or (Withdraw - 1) or (Check balance - 2) ")
            if(option == "0"):
                user.deposit()
            elif(option == "1"):
                user.withdraw()
            else:
                user.check_balance()
        else:
            print("Thanks for coming! see you again")
            break    
    else:
        option = input("Select any option (Deposit - 0) or (Withdraw - 1) or (Check balance - 2) ")
        if(option == "0"):
            user.deposit()
        elif(option == "1"):
            user.withdraw()
        else:
            user.check_balance()
    count = count + 1










