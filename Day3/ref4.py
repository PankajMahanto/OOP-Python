class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
def greed(customer):
    if customer.gender=='Male':
        print("Hello",customer.name,"sir")
    else:
        print("Hello",customer.name,"Maa'm")
    cust2 = Customer("Joy",'Male')
    return cust2

cust =Customer("Monira",'Female')

#Green ke call korbo
new=greed(cust)
print(new.name)