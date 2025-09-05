class Customer:
    def __init__(self,name):
        self.name=name
        
def greed(customer):
    print("Hello",customer.name)
    

cust =Customer("Pankaj Mahanta")

#Green ke call korbo
greed(cust)