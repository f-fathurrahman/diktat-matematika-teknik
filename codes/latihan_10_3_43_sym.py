from sympy import *

z = symbols("z")

# Hitung sin^{-1}(10) dengan cara menyelesaikan persamaan sin(z) = 10
res = solve(cos(z) - 2.0, z)

rr = []
for r in res:
    rr.append( N(r) )
    print(N(r)) # ubah ke bentuk numerik
