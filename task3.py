# Demonstrating the use of user-defined decorator function

from package1.my_decorator import my_decorator   #importing 'my_decorator' function 
class Decorator:
    def __init__(self,a,b):
        self.num1 = a 
        self.num2 = b
          
    @my_decorator
    def sum(self):
        sum = self.num1 + self.num2
        print("Before modification =", sum) 
        return sum

obj = Decorator(10,20)
obj.sum()

# OUTPUT :-
*********************************************
Before modification = 30
After modifying function =  40
*********************************************
