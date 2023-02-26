import mpmath

def my_func(x):
    return 1/(1 + x**2)

res = mpmath.quad(my_func, (0, mpmath.inf))
print("res = ", res)

