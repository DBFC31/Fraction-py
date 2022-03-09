import math

class fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)

        return self

    def inversed(self):
        return fraction(self.denominator, self.numerator)

    def __float__(self):
        return self.numerator/self.denominator

    def __add__(self, f2):
        
        sn = self.numerator * f2.denominator
        sd = self.denominator * f2.denominator

        n = f2.numerator * self.denominator

        r = fraction(sn + n, sd)
        print(r.numerator, r.denominator)

        r.simplify()
        return r

    def __sub__(self, f2):
        sn = self.numerator * f2.denominator
        sd = self.denominator * f2.denominator

        n = f2.numerator * self.denominator

        r = fraction(sn - n, sd)
        print(r.numerator, r.denominator)

        r.simplify()
        return r

    def __mul__(self, f2):
        r = fraction(self.numerator * f2.numerator, self.denominator * f2.denominator)

        r.simplify()
        return r
    
    def __truediv__(self, f2):
        r = self * f2.inversed()

        r.simplify()
        return r

    def __eq__(self, f2):
        self.simplify()
        f2.simplify()
        return self.numerator == f2.numerator and self.denominator == f2.denominator

    def __lt__(self, f2):
        aself = fraction(self.numerator*f2.denominator, self.denominator*f2.denominator)
        af2 = fraction(f2.numerator*self.denominator, f2.denominator*self.denominator)

        return aself.numerator < af2.numerator

    def __le__(self, f2):
        aself = fraction(self.numerator*f2.denominator, self.denominator*f2.denominator)
        af2 = fraction(f2.numerator*self.denominator, f2.denominator*self.denominator)
        
        return aself < af2 or aself == af2

    def __gt__(self, f2):
        aself = fraction(self.numerator*f2.denominator, self.denominator*f2.denominator)
        af2 = fraction(f2.numerator*self.denominator, f2.denominator*self.denominator)

        return aself.numerator > af2.numerator

    def __ge__(self, f2):
        aself = fraction(self.numerator*f2.denominator, self.denominator*f2.denominator)
        af2 = fraction(f2.numerator*self.denominator, f2.denominator*self.denominator)
        
        return aself > af2 or aself == af2


######## Debug ########

f1 = fraction(9, 6)
f2 = fraction(3, 2)

#12/6 + 9/6 = 21/6 = 7/2

r = f1/f2

print(0.1 + 0.2 == 0.3)