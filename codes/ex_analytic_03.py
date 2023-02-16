from sympy import *

init_printing()

z = symbols("z")
x, y = symbols("x y", real=True)

f = conjugate(z) * z**2
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
print("Cauchy-Riemann 1st:")
pprint(CR_eq1)

CR_eq2 = Equality(dudy, -dvdx)
print("Cauchy-Riemann 2nd:")
pprint(CR_eq2)

