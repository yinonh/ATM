import string

from dbRepository import dbReposetitory

class BankAccount:

    def init(self, account_number, name, password, balance):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.balance = float(balance)

    def __str__(self):
        return "Hello %s your account number is %s and there is a balance of %f NIS in you'r account" % \
               (self._name, self._account_number, self._balance)

    def log_in(self, account_number, password):
        account = dbReposetitory()
        details = account.get_account_details(account_number)
        if (details != None):
            if (password == details[2]):
                self.init(details[0], details[1], details[2], details[3])
                return True
        else:
            print("There is no such account number in the system")
        return False

    def check_invalid_input(self, name, password, amount):
        try:
            amount = float(amount)
        except:
            print("the amount have to be number")
            return False
        ABC = [x for x in string.ascii_letters]
        for i in name:
            if not (i in ABC or i == " "):
                print("%s is illegal character in name" % i)
                return False
        if (len(password) < 6 or len(password) > 20):
            print("The password have to be between 6 to 20 charactars")
            return False
        if not (any(i in password for i in ABC)):
            print("tha password should contain at least one letter")
            return False
        elif not (any(i in password for i in [str(x) for x in range(10)])):
            print("tha password should contain at least one number")
            return False
        else:
            return True

    def sing_up(self, name, password, amount=0):
        if not (self.check_invalid_input(name, password, amount)):
            return -1
        else:
            account = dbReposetitory()
            account_number = account.add_account(name.lower(), password, amount)
            return account_number

    def deposit(self, amount):
        try:
            amount = float(amount)
            if (amount < 0):
                raise Exception(ValueError)
            self._balance = float(self._balance) + amount
            print("Your deposit has successfully passed\nthere is balance of %f in you'r account" % (self._balance))
            return True
        except:
            print("the amount have to be number bigger then 0")
            return False

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if (amount < 0 or amount > self._balance):
                raise minus
            self._balance = float(self._balance) - amount
            print("Your withdraw has successfully passed\nthere is balance of %f in you'r account" % (self._balance))
            return True
        except minus:
            print("the amount have to be between 0 to %s " % (self._balance))
            print(minus())
            return False
        except:
            print("the amount have to be number")
            return False

    def log_out(self):
        updating = dbReposetitory()
        updating.updat(self._account_number, self._name, self._password, self._balance)