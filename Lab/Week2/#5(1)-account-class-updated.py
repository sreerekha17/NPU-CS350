
# Problem 5: Here are the Account and CheckingAccount classes:
# class Account():

#     """A bank account that allows deposits and withdrawals."""
#     interest = 0.02

#     def __init__(self, account_holder):
#         self.balance = 0
#         self.holder = account_holder

#     def deposit(self, amount):
#         """Increase the account balance by amount and return the new balance."""

#         self.balance = self.balance + amount
#         return self.balance

#     def withdraw(self, amount):
#         """Decrease the account balance by amount and return the new balance."""
        
#         if amount > self.balance:
#             return 'Insufficient funds'
        
#         self.balance = self.balance - amount
#         return self.balance


# class CheckingAccount(Account):
#     """A bank account that charges for withdrawals."""

#     withdraw_fee = 1
#     interest = 0.01

#     def withdraw(self, amount):
#         return Account.withdraw(self, amount + self.withdraw_fee)
# Create a new class by inheritance with a new attribute, transactions, which is a list keeping track of any transactions performed as following example

# Lindell_account = inheritsFromNewChildClass("Lindell")
# Lindell_account.deposit(12345)   	# depositing my paycheck for the week
# 12345
# Lindell_account.transactions
# [('deposit', 12345)]
# Lindell_account.withdraw(100)      	# buying dinner
# 12245
# Lindell_account.transactions
# [('deposit', 12345),('withdraw', 100)]

############### Solution ###########################
class Account():
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        super().__init__()
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if (amount > self.balance):
            return 'Insufficient Funds'
        self.balance = self.balance - amount
        return self.balance
    
class CheckingAccount(Account):
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

class CheckingAccountWithMonitoring(CheckingAccount): #Extending CheckingAccount class which records transactions 
    def __init__(self, account_holder):
        self.transactions = []
        CheckingAccount.__init__(self, account_holder)

    def recordTransactions(transactionType):
        def recordTransactionType(method):
            def innerFunction(*args):
                self = args[0]
                self.transactions.append((transactionType, args[1]))
                method(*args)
            return innerFunction
        return recordTransactionType

    @recordTransactions("deposit")
    def deposit(self, amount):
        return CheckingAccount.deposit(self, amount)
    
    @recordTransactions("withdraw")
    def withdraw(self, amount):
        return CheckingAccount.withdraw(self, amount)


Lindell_account = CheckingAccountWithMonitoring("Lindell")

Lindell_account.deposit(12345)
print(Lindell_account.transactions)

Lindell_account.withdraw(100)
print(Lindell_account.transactions)

