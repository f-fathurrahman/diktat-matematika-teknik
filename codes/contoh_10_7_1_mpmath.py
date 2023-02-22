import mpmath

I = mpmath.sqrt(-1)
def my_func(θ):
    z = 0.5 + mpmath.exp(I*θ)
    dz = I * mpmath.exp(I*θ)
    return z**2/(z**2 - 1) * dz

res = mpmath.quad(my_func, (0, 2*mpmath.pi))
print("res = ", res)
# should be close to I*π

# Mathematica??
# Integrate[ (1/2 + Exp[I*t])^2/( (1/2 + Exp[I*t])^2 - 1) * I * Exp[I*t] ]