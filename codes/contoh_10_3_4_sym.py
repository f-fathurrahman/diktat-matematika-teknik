from sympy import *

z = symbols("z")

# Hitung sin^{-1}(10) dengan cara menyelesaikan persamaan sin(z) = 10
res = solve(sin(z) - 10.0, z)
# 10.0: gunakan floating point

for r in res:
    print(N(r)) # ubah ke bentuk numerik
