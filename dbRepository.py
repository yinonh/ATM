import csv
from Reposeitory import Reposetory

class dbReposetitory (Reposetory):

    def add_account(self, name, password, amount=0):
        with open("ATMdeata.csv", "r") as db:
            accounts_number = int(db.readline().split(",")[4]) + 1
            with open("temp.csv", "w") as temp:
                reader = csv.reader(db)
                temp.write("account number,name,password,balance,%s\n" % (accounts_number))
                for row in reader:
                    temp.write(','.join(row))
                    temp.write("\n")
                temp.write("%s,%s,%s,%s" % (str(accounts_number), name, password, amount))
        with open("ATMdeata.csv", "w") as db:
            with open("temp.csv", "r") as temp:
                for i in temp:
                    db.write(i)
        return accounts_number

    def get_account_details(self, number):
        number = str(number)
        with open("ATMdeata.csv", "r") as db:
            for account in db:
                account = account.split(",")
                if account[0] == number:
                    db.close()
                    return account[:4]
        return None

    def updat(self, account_number, name, password, balance):
        result = False
        with open("ATMdeata.csv", "r") as db:
            with open("temp.csv", "w") as temp:
                for account in db:
                    if account.split(",")[0] == account_number:
                        temp.write("%s,%s,%s,%s,\n" % (account_number, name, password, balance))
                        resutl = True
                    else:
                        temp.write(account)
        with open("ATMdeata.csv", "w") as db:
            with open("temp.csv", "r") as temp:
                for i in temp:
                    db.write(i)
        return result
