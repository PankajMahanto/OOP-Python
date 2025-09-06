'''
w3resource website
1. Circle Class for Area and Perimeter

Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

'''
import math
class Circle:
    
    #constructor
    def __init__(self,r):
        self.r=r
        self.Area()
        self.Perimeter()
        
    
    def Area(self):
        a = 2*math.pi*self.r**2
        return "Area is: {}".format(a)
    
    def Perimeter(self):
        peri = 2*math.pi*self.r
        
        return "Perimeter: {}".format(peri)   


c1 = Circle(4)
print(c1.Perimeter())
print(c1.Area())

c2 = Circle(5)
print(c2.Perimeter())
print(c2.Area())
