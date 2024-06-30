from sympy import *
init_printing()

z = symbols("z")
t = symbols("t")
num1 = exp(z*t)
denum1 = z**2 * (z**2 + 2*z + 2)
f = num1/denum1

rr = list( roots(denum1).keys() )
# There are three roots
res1 = residue(f, z, rr[0])
pprint(simplify(res1))

res2 = residue(f, z, rr[1])
pprint(simplify(res2))

res3 = residue(f, z, rr[2])
pprint(simplify(res3))


# Sum of residues
sum_res = simplify(res1 + res2 + res3)
print("sum_res = ")
pprint(sum_res)

#res_int = N(sum_res)
#print("res_int = ", res_int)


