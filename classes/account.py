class Bank:
    def __init__(self, account_number, balance, interest_rate):
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
    
    def check_balance(self):
        return f"Your current account balance is ${self.balance}"
    

    def deposit(self, amount):
        self.balance += amount
        transaction = {"amount": amount, "narration": "deposit"}
        self.deposits.append(transaction)
        return f"Your deposit of ${amount} was successful. Your new balance is ${self.balance}"
    

    def withdraw(self, amount):
        if amount > self.balance:
            return f"Insufficient funds. Your current balance is ${self.balance}"
        else:
            self.balance -= amount
            transaction = {"amount": amount, "narration": "withdrawal"}
            self.withdrawals.append(transaction)
            return f"Your withdrawal of ${amount} was successful. Your new balance is ${self.balance}"


    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")


    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            return "You already have an outstanding loan"
        elif amount <= 100:
            return "Loan amount must be greater than 100"
        elif len(self.deposits) < 10:
            return "You must have made at least 10 deposits to be eligible for a loan"
        elif amount > sum([deposit['amount'] for deposit in self.deposits])/3:
            return "Loan amount requested is more than 1/3 of your total deposits"
        else:
            self.loan_balance += amount
            return f"Your loan of ${amount} was successful. Your new loan balance is ${self.loan_balance}"


    def repay_loan(self, amount):
        if amount > self.loan_balance:
            self.balance += amount - self.loan_balance
            self.loan_balance = 0
            return f"You have successfully repaid your loan. Your new balance is ${self.balance}"
        else:
            self.loan_balance -= amount
            return f"You have successfully repaid ${amount} of your loan. Your new loan balance is ${self.loan_balance}"  

    
    def transfer(self, amount, account):
        if amount > self.balance:
            return f"Insufficient funds. Your current balance is ${self.balance}"
        else:
            self.balance -= amount
            account.deposit(amount)
            return f"You have successfully transferred ${amount} to account {account.account_number}. Your new balance is ${self.balance}"

# Create a new bank account with initial balance of $1000 and an interest rate of 5%
my_account = Bank("7770178528995", 10000, 0.05)

# Check the account balance
print(my_account.check_balance())  

# Make a deposit of $500
print(my_account.deposit(2000))  

# Make a withdrawal of $200
print(my_account.withdraw(5000)) 

# Print a statement of all transactions
my_account.print_statement() 

# Borrow a loan of $500
print(my_account.borrow_loan(1500))  

# Repay $200 of the loan
print(my_account.repay_loan(1200))

# Transfer $100 to another account
other_account = Bank("77727560770", 0, 0)
print(my_account.transfer(1000, other_account)) 