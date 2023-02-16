from sympy import *

init_printing()

z = symbols("z")
x, y = symbols("x y", real=True)

u = x**2 - y**2
v = 2*x*y

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
