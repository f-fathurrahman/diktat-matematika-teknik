from sympy import *

init_printing()

z = symbols("z")
x, y = symbols("x y", real=True)

f = sin(z)*cos(2*z)
#f = (z**2 + z + 1) / (z**3 + 3*z + 1) 
fxy = expand( f.subs({z: x + I*y}) )

pprint(fxy)

u = re(fxy)
v = im(fxy)
print("u = "); pprint(u)
print("v = "); pprint(v)

dudx = simplify(diff(u, x))
dudy = simplify(diff(u, y))
pprint(dudx)
pprint(dudy)

dvdx = simplify(diff(v, x))
dvdy = simplify(diff(v, y))
pprint(dvdx)
pprint(dvdy)


CR_eq1 = Equality(dudx, dvdy)
pprint(CR_eq1)

CR_eq2 = Equality(dudy, -dvdx)
pprint(CR_eq2)

