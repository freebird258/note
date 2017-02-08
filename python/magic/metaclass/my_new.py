# encoding: utf-8
#!/usr/bin/env python

class Person(object):
    """Silly Person"""
    def __new__(cls,name,age):
        print'__new__ called.'
        return super(Person,cls).__new__(cls,name,age)
 
    def __init__(self,name,age):
        print'__init__ called.'
        self.name=name
        self.age=age
 
    def __str__(self):
        return'<Person: %s(%s)>'%(self.name,self.age)

class PositiveInteger(int):
#   def __new__(cls,value):
 #      return super(PositiveInteger,cls).__new__(cls,abs(value))
   def __init__(self, value):
        super(PositiveInteger, self).__init__(self, abs(value)) 

if __name__=='__main__':
    piglei = Person('piglei',24)
    print piglei

    i= PositiveInteger(-3)
    print i
