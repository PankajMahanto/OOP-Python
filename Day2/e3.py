
#! WORKING on ENCAPSULATION
class Atm:

    #! Constructor
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        #! Manu method call here
        self.__manu()
        
        
        
    
    #! Getter method
    def get_pin(self):
        return self.__pin
    
    #! Setter Method
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
        else:
            print("Type Mismatch.....!!!!")
    

    def __manu(self):
        user_input = input(
            """
        Hello, Welcome to Our ATM system.
            1. Create Your Pin.
            2. Deposit Your Balance.
            3. Withdraw Your Balance.
            4. Check Your Current Balanced.
            5. Exit.                 
                    """
        )

        if user_input == "1":
            print("Create Pin")
            self.create_pin()

        elif user_input == "2":
            print("Deposit")
            self.deposit()

        elif user_input == "3":
            print("Withdraw Balanced")
            self.withdraw()

        elif user_input == "4":
            print("Check Balance")
            self.check_balance()

        else:
            print("Exit")

    def check_pin(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print("Access Granted....")
            return 1
        else:
            print("Invalid Pin Try again!!!")
            return 0

    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Create Pin Successfully")
        self.__manu()

    def deposit(self):
        if self.check_pin()==1:
            amount = int(input("Enter your Amount: "))
            self.__balance += amount
            print("Deposit Successful")
        else:
            print("Try Again!!...")

        self.__manu()

    def withdraw(self):
        if self.check_pin()==1:
            amount = int(input("Enter your withdraw amount: "))
            if self.__balance>=amount:
                self.__balance -= amount
                print("Withdraw Successful.")
            else:
                print("Insufficient Fund!!!.....")
        else:
            print("Try Again!!.....")

        self.__manu()

    def check_balance(self):
        if self.check_pin()==1:
            print("Current balanced: ", self.__balance)
        else:
            print("Try Again!!!.....")

        self.__manu()
