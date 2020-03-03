class NewAtmData ():
    def Open_New_Db(self, name="ATMdata"):
        with open (name,"w") as db:
            db.write("account number,name,password,balance,%s\n" % 0)

