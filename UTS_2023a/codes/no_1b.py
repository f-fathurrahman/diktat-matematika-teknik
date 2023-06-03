from my_complex_funcs import *

z = 3 + 4j

rr = my_complex_power(z, 1 - 1j, k=0)
print(rr)
print(cmplx2polar(rr))

print("Built-in result:")
print(z**(1-1j))

