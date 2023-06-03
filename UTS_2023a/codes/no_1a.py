from my_complex_funcs import *
z = 3 + 4j

for k in range(0,4):
    print("k = ", k + 1)
    rr = my_complex_power(z, 1/4, k=k)
    print(rr)
    print(cmplx2polar(rr))

