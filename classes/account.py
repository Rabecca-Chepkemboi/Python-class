class Account:
    type = "savings"
    def __init__(self, account_number, balance, owner, amount):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.amount = amount
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0


# 3. Update the deposit method to append each withdrawal transaction to the deposits list.
# Each transaction should be in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }
    def deposit(self, amount):
        self.balance += amount
        self.deposits.append({"amount":amount, "narration":"deposit"})
        print(f"You have deposited {amount} into account {self.account_number} and the new balance is {self.balance}.")


# 4. Update the withdrawal method to append each withdrawal transaction to the withdrawals list.
# Each transaction should be in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }

    def withdraw(self, amount):
        if amount > self.balance:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
            print("You have Insufficient funds.")
        else:
            self.balance -= amount
            self.withdrawals.append({"amount":amount, "narration":"withdrawal"})
            print(f"Withdrew {amount} from account {self.account_number} and the new balance is {self.balance}.")

# 2. Add a method check_balance which returns the account’s balance

    def find_balance(self):
        print(f"The balance of account {self.account_number} is {self.balance}.")


# 5. Add a new method  print_statement which combines both deposits and withdrawals into one 
# list and, using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500

    def output_statement(self):
        for transaction in self.deposits + self.withdrawals:
            print(f"{transaction['narration']} - {transaction['amount']}")


# 6. Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount

    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            print("You already have an outstanding loan")
        elif amount <= 100:
            print("The loan amount must be more than 100")
        elif len(self.deposits) < 10:
            print("You must atleast have made upto 10 deposits before borrowing a loan")
        elif amount > sum([transaction[amount] for transaction in self.deposits])/3:
            print("Loan must excees 1/3 of total deposits")
        else:
            self.loan_balance += amount
            print(f"You have successful borrowed {amount}. Your loan balance is {self.loan_balance  }")


# 7. Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance

    def repay_loan(self, amount):
            if amount > self.loan_balance:
                self.balance +=(amount - self.loan_balance)
                self.loan_balance = 0
                print(f"Your loan have been repaid, your current balance is {self.balance}")
            else:
                self.loan_balance = amount
                print(f"Your loan balance is {self.loan_balance}")


# 8. Add a transfer method which accepts two attributes (amount and instance of another account). 
# If the amount is less than the current instances balance, the method transfers the requested 
# amount from the current account to the passed account. The transfer is accomplished by 
# reducing the current account balance and depositing the requested amount to the passed account.
                
    def transfer(self, amount, final_account):
        if amount > self.balance:
            print("You have insufficient funds, unfortunately you can't transfer")
        else:
            self.balance -= amount
            final_account.deposit(amount)
            print(f"You have transfered {amount} from {self.account_number} to account {final_account.account_number}")


account1 = Account("98765", 7900, "Clara Atenge", 5560)
account2 = Account("43678", 900, "Vince Auko", 7990)

account1.deposit(220)
account1.withdraw(140)
account1.output_statement()
account1.borrow_loan(200)
account1.repay_loan(155)
account1.find_balance()
account1.transfer(360, account2)
account1.find_balance()
account2.find_balance()