#  Challenge 5: 
#  andling a Bank Account

class Account:

    def __init__(self):
        self.title = 0
        self.balance = 0
        print("Welcome to the Deposit & Withdrawal Machine")

    def balance(self):
       self.title = "Ashish"
       self.balance = 2000
       print('Hello,', self.title, 'your balance is', self.balance)

    def withdrawal(self):
       amount = int(input("Enter amount to be Withdrawn: "))
       if self.balance>=amount:
            self.balance-=amount
            print("You Withdrew : ", amount, "\nNet balance is",self.balance)
       else:
            print("Insufficient balance  ")

    def deposit(self):
       amount=int(input("\nEnter amount to be Deposited : "))
       print("Amount Deposited :",amount)
       if amount >= 0:
         self.balance += amount
         print('Net bal is',self.balance)

class SavingsAccount(Account):

    def __init__(self):
        self.interestRate = 0
        return

    def display1(self):
      self.interestRate = 5
      self.interest = (self.interestRate * self.balance) / 100
      print('Interest rate is', self.interest)

obj = SavingsAccount()
obj.balance()
obj.withdrawal()
obj.deposit()
obj.display1()