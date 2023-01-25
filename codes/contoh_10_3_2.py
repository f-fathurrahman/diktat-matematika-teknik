# Hitung (2+i)^(1-i)

import cmath, math
# math: aritmatika dan fungsi real
# cmath: aritmatika dan fungsi kompleks

z1 = 2 + 1j
z2 = 1 - 1j
direct_pow = z1**z2 # using Python's built-in operator for power
print("direct_pow = ", direct_pow)


# representasi z1 dalam bentuk polar
r1 = math.sqrt(z1.real**2 + z1.imag**2)
θ1 = math.atan2(z1.imag, z1.real)
print("r1 = ", r1)
print("θ1 = ", θ1)

ln_z1 = math.log(r1) + 1j*θ1 # ln(z1), menggunakan aritmatika dan fungsi real
print("ln_z1 = ", ln_z1)


# Menggunakan fungsi kompleks
print("ln_z1 (using cmath): ", cmath.log(z1))

# (1 - i)*ln_z1
p1 = z2*ln_z1

# Hitung e^{x + iy} = e^x ( cos(y) + i*sin(y) )
# x: bagian real, y: bagian imajiner
res = math.exp(p1.real)*( math.cos(p1.imag) + 1j*math.sin(p1.imag) )
print("res = ", res)