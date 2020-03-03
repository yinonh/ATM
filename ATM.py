from Interface import Interface
def main():
    while True:
        user = Interface()
        choice = user.open_screen()
        if choice == 1:
            account = user.log_in()
            if account == None:
                continue
            else:
                while user.inner_screen(account):
                    pass
                account.log_out()
        else:
            user.sing_up()


if __name__ == "__main__":
    main()
