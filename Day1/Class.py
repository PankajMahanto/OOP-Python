# #! let's make a class


class Atm:

    #! function vs method
    """
    l = [1,2,3]
    len(l) #! eta ekta function

    l.append() #! eta ekta method

    function can use any one like list use and int o use kore
    but method only particular class object can uses.
    
    Class means -> Data types and methods
    -- class can access both data types and methods
    -- Only class object can access those two options
    -- 


    """

    def __init__(self): #! constructor 

        self.pin = ""
        self.balance = 0
        print("hello")

        self.manu()

    def manu(self):
        user_input = input('''
                            Hello now wolud like to proceed>
                            1. Enter 1 to create pin.
                            2. Enter 2 to deposit
                            3. Enter to 3 to withdraw
                            4. Enter 4 to check balanced
                            5. Enter 5 to exit
                           
                           
                           ''')
        if user_input == '1':
            print('Create pin')
        elif user_input == '2':
            print(" Deposite")
        elif user_input == '3':
            print("Withdraw")
        elif user_input == '4':
            print("Check balanced")
        else:
            print('Exit')