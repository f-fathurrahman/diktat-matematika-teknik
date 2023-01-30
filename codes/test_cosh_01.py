import math

# cosh(x) = (exp(x) + exp(-x))/2

x = 1.1

r1 = math.cosh(x)
print("r1 = ", r1)

r2 = ( math.exp(x) + math.exp(-x) ) / 2
print("r2 = ", r2)