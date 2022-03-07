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



######## Debug ########

f1 = fraction(6, 3)
f2 = fraction(3, 2)

#12/6 + 9/6 = 21/6 = 7/2

r = f1/f2

print(r.numerator, r.denominator)