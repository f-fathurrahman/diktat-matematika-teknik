from sympy import *

init_printing()

z = symbols("z")
x, y = symbols("x y", real=True)

f = z * z.conjugate()
fxy = expand( f.subs({z: x + I*y}) )

pprint(fxy)

u = re(fxy)
v = im(fxy)
print("u = "); pprint(u)
print("v = "); pprint(v)

dudx = diff(u, x)
dudy = diff(u, y)
pprint(dudx)
pprint(dudy)

dvdx = diff(v, x)
dvdy = diff(v, y)
pprint(dvdx)
pprint(dvdy)


CR_eq1 = Equality(dudx, dvdy)
pprint(CR_eq1)

CR_eq2 = Equality(dudy, -dvdx)
pprint(CR_eq2)

