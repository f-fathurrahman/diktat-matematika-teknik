from sympy import *

z = symbols("z")

res = solve(sin(z) - 2.0, z)

print("\nUsing sympy")
rr = []
for r in res:
    rr.append( N(r) )
    print(N(r)) # ubah ke bentuk numerik


from my_complex_funcs import my_arc_sin

print("\nUsing my_arc_sin")
res = my_arc_sin(2.0)
print(res)
