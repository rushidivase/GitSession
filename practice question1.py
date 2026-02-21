import os
import time

class ATM:

    def __init__(self):
        self.file = "account.txt"
        self.menu()
        
    def menu(self):
        print("Insert Your card")
        time.sleep(5)
        

        while True:

            print("\n===== ATM SYSTEM =====")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.register()

            elif choice == "2":
                self.login()

            elif choice == "3":
                print("Thank You")
                break

            else:
                print("Invalid choice")


    def register(self):

        name = input("Enter Name: ")
        pin = input("Create PIN: ")
        balance = input("Enter Initial Balance: ")

        with open(self.file, "w") as f:
            f.write(name + "\n")
            f.write(pin + "\n")
            f.write(balance)

        print("Registration Successful")


    def login(self):

        if not os.path.exists(self.file):

            print("No account found")
            return

        pin = input("Enter PIN: ")

        with open(self.file, "r") as f:

            data = f.readlines()

        if pin == data[1].strip():

            self.name = data[0].strip()
            self.pin = data[1].strip()
            self.balance = int(data[2].strip())

            print("Login Successful")

            self.dashboard()

        else:

            print("Wrong PIN")


    def dashboard(self):
        ch='Y'

        while (ch=="Y" or ch=="y"):

            print("\nWelcome", self.name)
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Logout")

            choice = input("Enter choice: ")

            if choice == "1":

                print("Balance:", self.balance)
                ch=input("Enter Do you want to continue??")

            elif choice == "2":

                amount = int(input("Enter amount: "))
                self.balance += amount
                self.update()
                print("Deposit Successful")
                ch=input("Enter Do you want to continue??")


            elif choice == "3":

                amount = int(input("Enter amount: "))

                if amount <= self.balance:

                    self.balance -= amount
                    self.update()
                    print("Withdraw Successful")
                    ch=input("Enter Do you want to continue??")

                else:

                    print("Insufficient Balance")
                    ch=input("Enter Do you want to continue??")


            elif choice == "4":

                new_pin = input("Enter new PIN")
                self.pin = new_pin
                self.update()
                print("PIN Changed")
                ch=input("Enter Do you want to continue??")


            elif choice == "5":

                break


            else:

                print("Invalid choice")


    def update(self):

        with open(self.file, "w") as f:

            f.write(self.name + "\n")
            f.write(self.pin + "\n")
            f.write(str(self.balance))


# Run project

obj = ATM()
