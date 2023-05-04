class Bank_Account:
    
    num_accounts = 0
   
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.name = name
       
        
        Account.num_accounts += 1
       
    def deposit(self, amount):
        self.balance += amount
       
           
    def get_account_number(self):
        return self.account_number
   
    def get_balance(self):
        return self.balance