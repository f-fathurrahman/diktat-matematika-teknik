import cmath, math

def cmplx2polar(z):
    x = z.real
    y = z.imag
    r = math.sqrt(x**2 + y**2)
    θ = math.atan2(y, x)
    return r, θ

def polar2cmplx(r, θ):
    re_part = r*math.cos(θ)
    im_part = r*math.sin(θ)
    return re_part + 1j*im_part

def my_log(z, k=0):
    r = math.sqrt(z.real**2 + z.imag**2)
    θ = math.atan2(z.imag, z.real)
    # Restrict to -π < θ <= π
    #if θ > math.pi:
    #    θ = 2*math.pi - θ
    return math.log(r) + 1j*(θ + 2*math.pi*k)


def my_arc_sin(z, k=0):
    r1 = 1j*z + cmath.sqrt(1 - z**2)
    r2 = 1j*z - cmath.sqrt(1 - z**2)
    return -1j*my_log(r1, k=k), -1j*my_log(r2, k=k)

def my_arc_cos(z, k=0):
    r1 = z + cmath.sqrt(z**2 - 1)
    r2 = z - cmath.sqrt(z**2 - 1)
    return -1j*my_log(r1, k=k), -1j*my_log(r2, k=k)


def my_complex_power(z, a, k=0):
    p = a*my_log(z, k=k)
    return cmath.exp(p)
