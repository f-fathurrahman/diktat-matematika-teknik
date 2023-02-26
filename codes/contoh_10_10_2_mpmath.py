import mpmath

def my_func(θ):
    return 1/(2 + mpmath.cos(θ))

res = mpmath.quad(my_func, (0, 2*mpmath.pi))
print("res = ", res)
# From the book: 3.628
