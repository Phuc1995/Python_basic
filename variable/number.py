a= 3
b= 4
s= a+b
print(s)
print(type(a))

from decimal import *
from fractions import *

# get max 30 number of phan nguyen va thap phan
getcontext().prec = 30

print(Decimal(10)/Decimal(3))

#phan so
a = Fraction(6,9)
print(a)
