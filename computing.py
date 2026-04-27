from math import factorial
class Computing:
    def __init__(self,number) -> None:
        self.number = number
    def Factorial(self):
        print("The fact is :",factorial(self.number))
    def Sum(self):
        i = 0
        sum =0
        while i <= self.number:
            sum += i
            i+=1
        print("The sum is :",sum)
    def tableMult(self):
        print("The Multiplication table of",self.number,"is ->")
        for i in range(1,11):
            print(f"{self.number} x {i} = {self.number*i}")
    def allTablesMult(self):
        for x in range(1,self.number+1):
            print("The Multiplication table of",x,"is ->")
            for y in range(1,11):
                print(f"{x} x {y} = {x * y}")
    def listDiv(self):
        Ldiv = []
        z = 1
        while z <=self.number:
            if self.number % z == 0:
                Ldiv.append(z)
            z = z + 1
        print("The list of divisors is :",Ldiv)
    def listDivPrim(self):
        LdivPrim = []
        for s in range(1,self.number + 1):
            if self.number % s == 0:
                for x in range(2,s):
                    if s % x != 0:
                        LdivPrim.append(s)
        print("The List of Prime divisors is :",LdivPrim)

num = Computing(10)
num.Factorial()
num.Sum()
num.tableMult()
num.allTablesMult()
num.listDiv()
# num.listDivPrim()
