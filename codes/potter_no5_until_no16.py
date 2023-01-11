import cmath

z = 3 - 4j
# or
# z = complex(3, -4)

no5 = z**2
print("no5 = ", no5)

no6 = z*z.conjugate()
print("no6 = ", no6)

no7 = z/z.conjugate()
print("no7 = ", no7)

no8 = cmath.polar( (z + 1)/(z - 1) )[0]
print("no8 = ", no8)