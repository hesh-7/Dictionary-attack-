import accinfo
class BankAccount:
    def __init__(self,account_number,name,balance) -> None:
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def deposit(self):
        before_balance = self.balance
        self.deposit_value = int(input("Enter Deposit Value : "))
        self.balance += self.deposit_value
        print(f"Deposit Successful!\n________________________\nDeposit : {self.deposit_value}$\nBalance Before Deposit : {before_balance}$\nBalance After Deposit : {self.balance}$")

    def withdrawal(self):
        before_balance = self.balance
        self.withdraw_value = int(input("Enter Withdraw Value : "))
        if self.withdraw_value > self.balance:
            print("Invalid Operation!\nInsufficient balance.")
            return -1
        else:
            self.balance -= self.withdraw_value
            print(f"Withdrawal Successful!\n________________________\nWithdraw : {self.withdraw_value}$\nYour Balance Before Withdrawal : {before_balance}$\nBalance After Withdrawal : {self.balance}$")
    def bankfees(self):
        before_balance = self.balance
        amountOfFee = (self.balance/100)*5
        self.balance = self.balance - (self.balance/100)*5
        print("Bank_Fee_Section:\n__________________________")
        print(f"Bank Fee is {amountOfFee} [5% of Your Total Balance]\nBalance Before Paying Fees : {before_balance}\nBalance After Paying Fees : {self.balance}")
    def display(self):
        print("Account Number :",self.account_number)
        print("Name :",self.name)
        print("Balance :",str(self.balance)+"$")
accno = input("Enter Account No:")
accno = "_"+ accno
acc_no = accinfo.accno["account_number"]
user_name = accinfo.accno["name"]
balance = accinfo.accno["balance"]
Hesham = BankAccount(acc_no,user_name,balance)
    
Hesham.display()
print("W - Withdraw\nD - Deposit\n")
i = input("What do you wanna do:").lower()
if i == "w":
    Hesham.withdrawal()
    Hesham.bankfees()
elif i == "d":
    Hesham.deposit()
    Hesham.bankfees()

Hesham.display()
