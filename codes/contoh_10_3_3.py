import cmath

z = 3 - 4j

bag_a = cmath.exp(1j*z)
print("bag_a = ", bag_a)

bag_b = cmath.exp(-1j*z)
print("bag_b = ", bag_b)

bag_c = cmath.sin(z)
print("bag_c = ", bag_c)

bag_d = cmath.log(z)
print("bag_d = ", bag_d)

