class Book:
    def __init__(self,n,p):
        self.name = n
        self.price = p
    def __add__(self,other):
        return Book("",self.price + other.price)
    def __str__(self):
        return f"total price of three = {self.price}"
    
b1 = Book("Cpp",200)
b2 = Book("Java",200)
b3 = Book("Python",200)
b4 = Book("Javascript",200)
b5 = Book("c",200)


res = b1 + b2 + b3 + b4 + b5
print(res)

# OUTPUT :
# total price of three = 1000