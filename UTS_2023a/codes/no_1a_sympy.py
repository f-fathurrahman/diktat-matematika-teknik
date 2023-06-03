from sympy import *

z0 = 3 + 4*I
z = symbols("z")
rr = roots(z**4 - z0)
for r in rr:
    print("Akar")
    pprint(r)
    pprint(N(r))
