# Hybrid Inheritance
class A:
    def m1(self):
        print("Class A:Method m1")
    
class B(A):
    def m2(self):
        print("Class B:Method m2")

class C(A):
    def m3(self):
        print("Class C:Method m3")

class D:
    def m4(self):
        print("Class D:Method m4")
    
class E(B):
    def m5(self):
        print("Class E:Method m5")

class F(C,D):
    def m6(self):
        print("Class F:Method m6")

jay = E()
viru = F()

jay.m1()
jay.m2()
jay.m5()

viru.m1()
viru.m3()
viru.m4()
viru.m6()

print(F.mro()) 
print(E.mro())

Output :
Class A:Method m1
Class B:Method m2
Class E:Method m5
Class A:Method m1
Class C:Method m3
Class D:Method m4
Class F:Method m6
[<class '__main__.F'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.D'>, <class 'object'>]
[<class '__main__.E'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
