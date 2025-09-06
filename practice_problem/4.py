'''
4. Shape Class with Subclasses for Different Shapes.
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

'''
import math
class Shape:
    # def __init__(self):
    #     print("Only")
    
    def area(self):
        print("Area method")
        pass
    
    def perimeter(self):
        print("Perimeter method")
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 2*math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
        
        

class Rectangle(Shape):
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
    def perimeter(self):
        return 2*(self.w+self.h)
    
class Square(Shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        return self.a**2
    def perimeter(self):
        return 4*self.a
class Triangle(Shape):
    def __init__(self,base,h,a,b,c):
        self.base=base
        self.h=h
        self.a=a
        self.b=b
        self.c=c
        
    def area(self):
        return 0.5*self.base*self.h
    def perimeter(self):
        return self.a+self.b+self.c


c=Circle(4)
print(c.area(),c.perimeter())
t=Rectangle(4,6)
print(t.area(),t.perimeter())

r = Triangle(3,5,4,5,6)
print(r.area(),r.perimeter())
s = Square(5)
print(s.area(),s.perimeter())

