from my_complex_funcs import cmplx2polar
import cmath

z = 2.0
r1 = 1j*z + cmath.sqrt(1 - z**2)
r2 = 1j*z - cmath.sqrt(1 - z**2)

print("r1 = ", r1)
print("r1 polar = ", cmplx2polar(r1))

print("r2 = ", r2)
print("r2 polar = ", cmplx2polar(r2))

#-1j*my_log(r1, k=k), -1j*my_log(r2, k=k)
