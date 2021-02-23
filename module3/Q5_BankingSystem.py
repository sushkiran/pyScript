'''
Q5. Design a software for bank system. There should be options like cash withdraw,
cash credit and change password. According to user input, the software should provide required output.
Hint: Use if else statements and functions
'''


class Password:

    def __init__(self, pwd):
        self.password = pwd

    def update(self, pwd):
        self.password = pwd

    def show(self):
        print('Current password is:', self.password)


class Account:

    def __init__(self, amount):
        self.balance_amt = amount

    def withdraw(self, amount):
        self.balance_amt -= amount

    def deposit(self, amount):
        self.balance_amt += amount

    def show_balance(self):
        text = 'Your balance is {:.2f} dollars'
        print(text.format(self.balance_amt))

    def is_zero_balance(self):
        return self.balance_amt == 0

    def get_balance(self):
        return self.balance_amt


def show_menu(acc, pwd):
    print('\n---- PY BANK ----')
    print('1. Cash Withdraw')
    print('2. Cash Deposit')
    print('3. Check Balance')
    print('4. Change Password')
    print('5. Exit')
    option = int(input("Enter option: "))
    process(option, acc, pwd)
    show_menu(acc, pwd)


def process(option, acc, pwd):
    if option == 1:
        acc.show_balance()
        if acc.is_zero_balance():
            print('You are bankrupt. Nothing to Withdraw.')
        else:
            withdraw(acc)
            acc.show_balance()

    elif option == 2:
        acc.show_balance()
        amount = int(input("Enter amount to deposit: "))
        acc.deposit(amount)
        print('Deposit Successful !!')
        acc.show_balance()

    elif option == 3:
        acc.show_balance()

    elif option == 4:
        pwd.show()
        new_pwd = input("Input new password: ")
        pwd.update(new_pwd)
        print('Password changed to', new_pwd)

    elif option == 5:
        exit()

    else:
        print('Incorrect Option. Please try again')


def withdraw(acc):
    amount = int(input("Enter amount to withdraw: "))
    if amount > acc.get_balance():
        print('Insufficient Funds to Withdraw.')
        withdraw(acc)
    else:
        acc.withdraw(amount)
        print('Withdrawal Successful !!')


def change_password():
    print('change_password')


if __name__ == "__main__":
    account = Account(200)
    password = Password('pwd123')
    show_menu(account, password)
