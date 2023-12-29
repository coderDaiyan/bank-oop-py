from Bank import Bank
from User import User, Admin
def main():
    citibank = Bank('Citi Bank')
    u1 = User('kala chan','kala@shada.com')
    u1.create_account('kalakalashadashada', citibank)
    u2 = User('kodu mia','kodu@jodu.com')
    u2.create_account('jodukodujodukodu', citibank)
    u1.deposit(500, citibank)
    u1.transfer_money(200, u2)
    # u1.check_transaction_history()
    a1 = Admin('xyz@gmail.com', 'xyz')
    a1.create_account('xyz', citibank)
    a1.toggle_loan(citibank)
    a1.toggle_loan(citibank)
    u1.take_loan(100, citibank)
    u2.withdraw(200, citibank)
    u1.withdraw(300, citibank)
    a1.toggle_loan(citibank)

if __name__ == '__main__':
    main()