from sympy import *

z = symbols("z")

# Hitung cos^{-1}(4) dengan cara menyelesaikan persamaan cos(z) = 4
res = solve(cos(z) - 4.0, z)

rr = []
for r in res:
    rr.append( N(r) )
    print(N(r)) # ubah ke bentuk numerik


from my_complex_funcs import my_arc_cos
print("\nUsing my_arc_cos")
res = my_arc_cos(4.0)
print(res)

