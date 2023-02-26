import mpmath

def my_func1(x):
    return mpmath.cos(x)/(1 + x**2)

def my_func2(x):
    return mpmath.sin(x)/(1 + x**2)

res1 = mpmath.quad(my_func1, (-mpmath.inf, mpmath.inf), maxdegree=10)
print("res1 = ", res1)

res2 = mpmath.quad(my_func2, (-mpmath.inf, mpmath.inf), maxdegree=10)
print("res2 = ", res2)

