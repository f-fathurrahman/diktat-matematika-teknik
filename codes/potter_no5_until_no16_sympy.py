from sympy import *

def cmplx2polar(z):
    x = re(z)
    y = im(z)
    r = N( sqrt(x**2 + y**2) )
    θ = N( atan2(y, x) ) # force numeric
    return r, θ

def polar2cmplx(r, θ):
    re_part = N(r*cos(θ))
    im_part = N(r*sin(θ))
    return re_part + I*im_part

z = 3 - 4*I

no5 = expand(z**2)
print("no5 = ", no5)

no6 = expand( z*z.conjugate() )
print("no6 = ", no6)

no7 = expand( z/z.conjugate() )
print("no7 = ", no7)

no8 = expand( (z + 1)/(z - 1) )
print("no8 = ", no8)

no9 = expand( (z + 1)*(z - I) )
print("no9 = ", no9)

no10 = expand( abs(z**2) )
print("no10 = ", no10)

no11 = expand( (z - I)**2 / (z - 1)**2 )
print("no11 = ", no11)

no12 = expand(z**4)

# Using root?

x = symbols("x")
#no13 = expand( z**Rational(1,2) )
no13 = roots(x**2 - z)
pprint(no13)

#no14 = expand( z**Rational(1,3) )
no14 = roots(x**3 - z)
pprint(no14)

#no15 = expand( z**Rational(2,3) )
no15 = [r**2 for r in no14]

no16 = expand( z**2/z**Rational(1,2) )