## Challenge 4: 
#  Implement a Banking Account

class Account:

    def __init__(self):
        self.title = 0
        self.balance = 0
        print("Welcome to the Deposit & Withdrawal Machine")

    def display(self):
      self.title = "Ashish"
      self.balance = 5000
      print('Hello,', self.title, 'your balance is', self.balance)

class SavingsAccount(Account):

    def __init__(self):
        self.interestRate = 0
        return

    def display1(self):
      self.interestRate = 5
      print('Interest rate is', self.interestRate,"%")

obj = SavingsAccount()
obj.display()
obj.display1()