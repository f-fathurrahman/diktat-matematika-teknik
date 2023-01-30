import math, cmath

z = math.pi/2 - 1j
# sin(z) = (exp(iz) - exp(-iz)) / (2i)
res1 = ( cmath.exp(1j*z) - cmath.exp(-1j*z) ) / (2j)
print("res1 = ", res1)

x = math.pi/2
y = -1
# sin(z) = sin(x)*cosh(y) + i sin(y)*cos(x)
res2 = math.sin(x)*math.cosh(y) + 1j * math.sin(y)*math.cos(x)
print("res2 = ", res2)


