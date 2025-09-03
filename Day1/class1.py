# #! let's make a class


class Atm:

    #! function vs method
    """
    l = [1,2,3]
    len(l) #! eta ekta function

    l.append() #! eta ekta method

    function can use any one like list use and int o use kore
    but method only particular class object can uses.


    """

    def __init__(self):  #! constructor

        self.pin = ""
        self.balance = 0
        print("hello")

        self.manu()

    def manu(self):
        user_input = input(
            """
                            Hello now wolud like to proceed>
                            1. Enter 1 to create pin.    BV
                            2. Enter 2 to deposit
                            3. Enter to 3 to withdraw
                            4. Enter 4 to check balanced
                            5. Enter 5 to exit
                           
                           
                           """
        )
        if user_input == "1":
            print("Create pin")
            self.create_pin()
            # self.manu()

        elif user_input == "2":
            print(" Deposite")
            self.Deposite()
            # self.manu()

        elif user_input == "3":
            print("Withdraw")
            self.withdraw()
            # self.manu()

        elif user_input == "4":
            print("Check balanced")
            self.check_balance()
            # self.manu()

        else:
            print("Exit")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Print Create Successfully")
        
        self.manu()

    def Deposite(self):

        temp = input("Enter your pin: ")
        if temp == self.pin:
            depo = int(input("Enter deposite amount> "))
            self.balance = self.balance + depo
        else:
            print(" Wrong password, Try again!")

        self.manu()
        
    def withdraw(self):

        temp = input("Enter your pin: ")
        if temp == self.pin:

            amount = int(input("enter your amount: "))
            if amount <= self.balance:
                print("withdraw Sucessfully Completed")
                self.balance = self.balance - amount
            else:
                print("Insufficient Balanced!")
        else:
            print("Wrong Password, Try again!")

        self.manu()
        
    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print("Current amount: ", self.balance)
        else:
            print("Wrong Password, Try Again!")

        self.manu() 