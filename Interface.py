from BankAccount import BankAccount

class Interface:
    def open_screen(self):
        x = input("Press 1 to log in\nPress 2 to sign up\n")
        while x != '1' and x != '2':
            x = input("please enter 1 or 2 only\n")
        if x == '1':
            return 1
        return 2

    def log_in(self):
        account_number = input("please enter you'r account number")
        password = input("please enter you'r password")
        account = BankAccount()
        result = account.log_in(account_number, password)
        if result:
            print("You have successfully connected")
            return account
        else:
            print("account or password are worng")
            return None

    def inner_screen(self, account):
        choice = input(
            "To make deposit enter 1\nTo make withdraw enter 2\nTo see your balance enter 3\nTo log out enter 4")
        if choice == '1':
            amount = input("enter the amount")
            account.deposit(amount)
        elif choice == '2':
            amount = input("enter the amount")
            account.withdraw(amount)
        elif choice == '3':
            print(account)
        elif choice == '4':
            return False
        else:
            print("choose between 1-4 only")
        return True

    def sing_up(self):
        name = input("please enter you'r name (English letters only):")
        password = input("please enter a password:")
        amount = input("if you want to add many yo you'r account please enter the amount else press enter") or 0
        account = BankAccount()
        account_number = account.sing_up(name, password, amount)
        if account_number != -1:
            print("you have successfully sing up you'r account number is %d\nyou need to use the account number to"
                  " log in" % account_number)
        return

    def log_out(self, account):
        account.log_out()
        self.open_screen()
