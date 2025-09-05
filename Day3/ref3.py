class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
def greed(customer):
    if customer.gender=='Male':
        print("Hello",customer.name,"sir")
    else:
        print("Hello",customer.name,"Maa'm")
    

cust =Customer("Monira",'Female')

#Green ke call korbo
greed(cust)