# a python program using a class to perform bank operations
class BankAccount:

    def __init__(self, account_number, date_of_opening, balance=0):
        self.account_number= account_number
        self.date_of_opening= date_of_opening
        self.balance=balance


    def deposit(self, deposited_amount):

        self.balance=+ deposited_amount

    def withdraw(self, deposited_amount):

        if self.balance>= deposited_amount:
            self.balance-= deposited_amount
        
        else:
            print("Sorry, you have insufficient funds in your account")

    def check_balance(self):

        return self.balance

    def customer_details(self):
        
        print("Name: Jeff Mwila")
        print("account number: 27547347")
        print("Acount opening date: 23-03-2022")

amount=BankAccount(27547347,"23-03-2022", balance=0)

print(amount.customer_details())
amount.deposit(20000)
print("You have successfuly deposited Ksh 20000. Your account balance is=", amount.check_balance())

amount.withdraw(5000)
print("You have successfuly withdrawn Ksh 5000. Your remaining account balance is=", amount.check_balance())



        