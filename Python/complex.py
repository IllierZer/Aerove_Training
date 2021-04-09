import math
class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def display(self):
        if(-1*self.b<0):
            print(str(self.a)+" +"+str(self.b)+"i")
        else:
            print(str(self.a)+" -"+str(abs(self.b))+"i")

        
    
    def add(self,c):
        sum=Complex(c.a+self.a,c.b+self.b)
        return sum
    
    def sub(self,c):
        diff=Complex(self.a-c.a,self.b-c.b)
        return diff

    def conjugate(self):
        c=Complex(self.a,-self.b)
        return c
    def mod(self):
        c=math.sqrt(self.a*self.a+self.b*self.b)
        return c

    def multiply(self ,c):
        product= Complex(self.a*c.a-self.b*c.b, self.a*c.b+self.b*c.a)
        return product

    def inverse(self):
        return Complex((self.a)/self.mod(),-self.b/self.mod())










        
    

        