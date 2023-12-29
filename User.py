class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.hasAccount = False
        self.__balance = 0
        self.__loan = 0
        self.__transactions = []

    def create_account(self, password, bank):
        bank._users.append({'email': self.email, 'password': password})
        self.hasAccount = True

    def deposit(self, amount, bank):
        if self.hasAccount:
            self.__balance += amount
            bank._balance += amount
            self.__transactions.append({'type': 'deposit', 'amount': amount})
        else:
            print("Please create an account")
    
    def withdraw(self, amount, bank):
        if self.hasAccount:
            if bank._balance >= amount:
                if(amount <= self.__balance):
                    self.__balance -= amount
                    bank._balance -= amount
                    self.__transactions.append({'type': 'withdraw', 'amount': amount})
                else:
                    print(f'Not enough balance in your account')
            else:
                print(f'Bank is bankrupt.')
        else:
            print("Please create an account")

    def check_balance(self):
        if self.hasAccount:
            print(self.__balance)
        else:
            print("Please create an account")    

    def transfer_money(self, amount, reciever):
        if self.hasAccount and reciever.hasAccount:
            self.__balance -= amount
            reciever.__balance += amount
            self.__transactions.append({'type': 'transfer', 'sender': self.name, 'reciever': reciever.name, 'amount': amount})
        else:
            print("Please create an account")

    def check_transaction_history(self):
        if self.hasAccount:
            for transaction in self.__transactions:
                if(transaction['type'] == 'transfer'):
                    print(f'{transaction['type']}ed from {transaction['sender']} to {transaction['reciever']} - {transaction['amount']}')
                else:
                    print(f'{transaction['type']} - {transaction['amount']}')
        else:
            print("Please create an account")

    def take_loan(self, amount, bank):
        if self.hasAccount:
            if bank.loanAvailable:
                if(amount <= (self.__balance * 2)):
                    self.__balance += amount
                    self.__loan = amount
                    bank._total_loan += 1
                    bank._balance -= amount
                else:
                    print(f'You can not take loan more than twice of your balance')
            else:
                print('Loan not available')
        else:
            print("Please create an account")

class Admin(User):
    def __init__(self, email, name) -> None:
        self.hasAccount = False
        super().__init__(email, name)
    
    def create_account(self, password, bank):
        bank._admins.append({'email': self.email, 'password': password})
        self.hasAccount = True

    def balance_of_bank(self, bank):
        print(bank._balance)
    
    def total_loan(self, bank):
        print(bank._total_loan)

    def toggle_loan(self, bank):
        if self.hasAccount:
            bank.loanAvailable = not bank.loanAvailable
        else:
            print("Please create an account")



