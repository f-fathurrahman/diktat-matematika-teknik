from my_complex_funcs import my_arc_sin

z = 2

r1, r2 = my_arc_sin(z)
print("r1 = ", r1)
print("r2 = ", r2)

import cmath
print("Built-in: ", cmath.asin(z))
