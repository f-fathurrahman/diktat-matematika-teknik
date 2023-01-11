from sympy import *

def to_polar(z):
    x = re(z)
    y = im(z)
    mag = a

z = 3 - 4*I

no5 = z**2
print("no5 = ", no5)

no6 = z*z.conjugate()
print("no6 = ", no6)

no7 = z/z.conjugate()
print("no7 = ", no7)

no8 = (z + 1)/(z - 1)
print("no8 = ", no8)