"""
2. Person Class with Age Calculation

Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
"""


class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

        # self.age_dob()

    def age_dob(self):
        d = self.dob.split("-")
        date = int(d[0])
        month=int(d[1])
        year=int(d[2])
        c_year=2025
        c_m=9
        c_d=6
        age = c_year-year
        if c_m <month and c_d<date :
            age-=1
        return age

person = Person("Joy", "BD", "10-08-2001")
age = person.age_dob()
print(person.name," ",person.country," ","dob: ",person.dob)
print("\nAge: ",age)

print("---------------")
print("Version-------")
print("-----------2")

from datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
        
        # self.calculate_age()
    
    
    def calculate_age(self):
        today = date.today()
        age = today.year-self.dob.year
        
        if today<date(self.dob.year,self.dob.month,self.dob.day):
            age-=1
        return age
        

person = Person('Joy',"BD",date(2001,8,10))

print(person.calculate_age())