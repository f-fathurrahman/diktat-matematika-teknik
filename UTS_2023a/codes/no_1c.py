from my_complex_funcs import my_log, cmplx2polar
import cmath
z = -5 + 12j

r = cmath.log(z)
print("Using cmath: ", r)
print("Polar = ", cmplx2polar(r))

print("Using my_log: ", my_log(z))
