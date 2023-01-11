#z = 4 + 3j
z = -4 + 3j

print(z.real)
print(z.imag)

# Convert to polar form
import cmath
zpolar = cmath.polar(z)
print("Magnitude: ", zpolar[0])
print("Angle (radian): ", zpolar[1])
print("Angle (degree): ", zpolar[1]*180/cmath.pi)

