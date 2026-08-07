class fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)
    def __mul__(self, diff):
        return fraction(self.numerator*diff.numerator, self.denominator*diff.denominator)
    
#-----------------------------------------------------------------
a=fraction(2,3)
b=fraction(3,7)
print(a)
print(a*b)