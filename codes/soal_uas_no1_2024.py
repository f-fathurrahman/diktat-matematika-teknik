import mpmath

I = mpmath.sqrt(-1)
def my_func(θ):
    z = 3*mpmath.exp(I*θ) # circle with radius 3, centered on (0,0)
    dz = 3*I*mpmath.exp(I*θ) # due to substitution z = 3*e^{iθ} -> dz = 3*i*e^{iθ}
    f1 = mpmath.exp(z)
    f2 = z**2 * (z**2 + 2*z + 2)
    return f1/f2 * dz

res_int = mpmath.quad(my_func, (0, 2*mpmath.pi))
print("res_int = ", res_int)

print("res = ", res_int/(2*mpmath.pi*I))