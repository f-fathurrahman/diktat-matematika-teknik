import cmath, math

def my_log(z, k=0):
    r = math.sqrt(z.real**2 + z.imag**2)
    θ = math.atan2(z.imag, z.real)
    return math.log(r) + 1j*(θ + 2*math.pi*k)


def my_arc_sin(z):
    r1 = 1j*z + cmath.sqrt(1 - z**2)
    r2 = 1j*z - cmath.sqrt(1 - z**2)
    return -1j*cmath.log(r1), -1j*cmath.log(r2)

def my_arc_cos(z):
    r1 = z + cmath.sqrt(z**2 - 1)
    r2 = z - cmath.sqrt(z**2 - 1)
    return -1j*cmath.log(r1), -1j*cmath.log(r2)
