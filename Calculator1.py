class calc:
    def add(self):
        print("enter numbers to add:")
        a = int(input())
        b = int(input())
        sum = a + b
        return sum
    def sub(self):
        print("enter numbers to subtract:")
        a = int(input())
        b = int(input())
        sub = a - b
        return sub
    def mul(self):
        print("enter numbers to Multiply:")
        a = int(input())
        b = int(input())
        mul = a * b
        return mul
    def div(self):
        print("enter numbers to Divide:")
        a = int(input())
        b = int(input())
        div = a / b
        return div
    def __init__(self):
        print("""Menu
            1.Addition
            2.Subtraction
            3.Multiplication
            4.Division
        """)
        try:
            choice = int(input("Enter your choice :"))
        except Exception as e:
            print("Enter valid choice....")
        else:
            if(choice == 1):
                print(self.add())
            elif(choice == 2):
                print(self.sub())
            elif(choice == 3):
                print(self.mul())
            elif(choice == 4):
                print(self.div())   
            else:
                print("invalid choice")

calc()