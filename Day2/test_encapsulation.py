
'''  
from pan import Atm
dbbl = Atm()

        Hello, Welcome to Our ATM system.
            1. Create Your Pin.
            2. Deposit Your Balance.
            3. Withdraw Your Balance.
            4. Check Your Current Balanced.
            5. Exit.                 
                    5
Exit
dbbl.manu()

        Hello, Welcome to Our ATM system.
            1. Create Your Pin.
            2. Deposit Your Balance.
            3. Withdraw Your Balance.
            4. Check Your Current Balanced.
            5. Exit.                 
                    1
Create Pin
Enter your pin: 123
Create Pin Successfully

        Hello, Welcome to Our ATM system.
            1. Create Your Pin.
            2. Deposit Your Balance.
            3. Withdraw Your Balance.
            4. Check Your Current Balanced.
            5. Exit.                 
                    2
Deposit
Enter your pin: 50000
Invalid Pin Try again!!!
Try Again!!...

        Hello, Welcome to Our ATM system.
            1. Create Your Pin.
            2. Deposit Your Balance.
            3. Withdraw Your Balance.
            4. Check Your Current Balanced.
            5. Exit.                 
                    dbbl.check_balance()
Exit
dbbl.check_balance()
Enter your pin: 123
Access Granted....
Current balanced:  0

        Hello, Welcome to Our ATM system.
            1. Create Your Pin.
            2. Deposit Your Balance.
            3. Withdraw Your Balance.
            4. Check Your Current Balanced.
            5. Exit.                 
                    5
Exit
dbbl.pin
'123'
dbbl.pin = "321"

dbbl.pin
'321'
dbbl.manu(
    )

        Hello, Welcome to Our ATM system.
            1. Create Your Pin.
            2. Deposit Your Balance.
            3. Withdraw Your Balance.
            4. Check Your Current Balanced.
            5. Exit.                 
                    2
Deposit
Enter your pin: 321
Access Granted....
Enter your Amount: 30000
Deposit Successful

        Hello, Welcome to Our ATM system.
            1. Create Your Pin.
            2. Deposit Your Balance.
            3. Withdraw Your Balance.
            4. Check Your Current Balanced.
            5. Exit.                 
                    5
Exit
dbbl.balance
30000
dbbl.balance="Pankaj"

dbbl.check_
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    dbbl.check_
AttributeError: 'Atm' object has no attribute 'check_'. Did you mean: 'check_pin'?

dbbl.check_balance()
Enter your pin: 321
Access Granted....
Current balanced:  Pankaj

        Hello, Welcome to Our ATM system.
            1. Create Your Pin.
            2. Deposit Your Balance.
            3. Withdraw Your Balance.
            4. Check Your Current Balanced.
            5. Exit.                 
                    2
Deposit
Enter your pin: 321
Access Granted....
Enter your Amount: 500
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dbbl.check_balance()
  File "C:\Users\HP\AppData\Local\Programs\Python\Python313\pan.py", line 85, in check_balance
    self.manu()
  File "C:\Users\HP\AppData\Local\Programs\Python\Python313\pan.py", line 29, in manu
    self.deposit()
  File "C:\Users\HP\AppData\Local\Programs\Python\Python313\pan.py", line 59, in deposit
    self.balance += amount
TypeError: can only concatenate str (not "int") to str

'''