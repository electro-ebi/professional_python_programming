import pandas as pd
import datetime
import sys

class Customer:
    bankname = 'INDIAN BANK OF AVADI'

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def _update_transaction_data(self, transaction_type, amount):
        
        transaction = {
        	"Type": transaction_type, 
        	"Date": datetime.datetime.now(), 
        	"Amount": amount, 
        	"Balance": self.balance
        	}
        self.transactions.append(transaction)
        return transaction

    def amountcredit(self, amt):
        self.balance += amt
        transaction = self._update_transaction_data("credit", amt)
        print(f'Balance after depositing {transaction["Amount"]}: {self.balance}')

    def withdraw(self, amt):
        if amt > self.balance:
            print('Insufficient Amount.....cannot perform this operation')
            sys.exit()
        else:
            self.balance -= amt
            transaction = self._update_transaction_data("debit", amt)
            print(f'Balance after withdrawing {transaction["Amount"]}: {self.balance}')

    def balance_enquiry(self):
        print('Available balance is : ', self.balance)

    def mini(self):
        mini_statement = pd.DataFrame(self.transactions)
        print(mini_statement)

print("WELCOME TO"+Customer.bankname)
name = input('Enter Your Name : ')
last_digits = input("Enter the last digits of ATM : ")
PIN = input("Enter the PIN : ")
c = Customer(name)

while True:
    print('1-Deposit \n2-Withdraw \n3-balance_enquiry\n4-mini statement\n5-exit')
    option = input('Choose your option : ')

    if option == '1':
        amt = float(input('Enter amount : '))
        c.amountcredit(amt)

    elif option == '2':
        amt = float(input('Enter amount : '))
        c.withdraw(amt)

    elif option == '3':
        c.balance_enquiry()

    elif option == '4':
        c.mini()
        print("Your mini statement is")

    elif option == '5':
        print('Thanks for Banking with INDIAN BANK')
        sys.exit()

    else:
        print('Invalid option..Plz choose a valid option')

