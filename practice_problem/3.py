'''
3. Calculator Class for Basic Arithmetic Operations

Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
'''
##! Make simple calculator
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    
    def arithmetic_operation(self):
        add = self.a+self.b
        print("add: ",add)
        sub = self.a-self.b
        print('Sub: ',sub)
        mul=self.a*self.b
        print("Mul: ",mul)
        if self.b>0:
            div=self.a//self.b
            print('Div: ',div)
            
        mod=self.a%self.b
        print("Mod: ",mod)


t=Calculator(10,7)

t.arithmetic_operation()