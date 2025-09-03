'''

Create own dataset using fraction 
method like: add,sub, mul,div mod


'''
class Fraction:
    
    def __init__(self,n,d):
        self.num=n
        self.den=d
        
        
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):
        
        temp_n = self.num*other.den +self.den*other.num
        temp_d = self.den*other.den

        return "{}/{}".format(temp_n,temp_d)
    
    def __sub__(self,other):
        
        temp_n = self.num*other.den - self.den*other.num
        temp_d = self.den*other.den

        return "{}/{}".format(temp_n,temp_d)
    
    
    def __mul__(self,other):
        
        temp_n = self.num*other.num
        temp_d = self.den*other.den

        return "{}/{}".format(temp_n,temp_d)
    
    def __truediv__(self,other):
        
        temp_n = self.num*other.den
        temp_d = self.den*other.num

        return "{}/{}".format(temp_n,temp_d)