import mpmath

I = mpmath.sqrt(-1)
def my_func(θ):
    r = 2.0 # radius
    center = 1.0
    z = center + r*mpmath.exp(I*θ)
    dz = r * I * mpmath.exp(I*θ)
    return z**2/(z - 2) * dz

res = mpmath.quad(my_func, (0, 2*mpmath.pi), degree=10)
print("res = ", res)
