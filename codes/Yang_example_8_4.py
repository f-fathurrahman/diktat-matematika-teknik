import numpy as np
import matplotlib.pyplot as plt

V0 = 1.0

def calc_phi(x,y):
    return V0*(x + x/(x**2 + y**2))

def calc_psi(x,y):
    return V0*(y - y/(x**2 + y**2))


def calc_u(x,y):
    return V0*( 1 - (x**2 - y**2)/(x**2 + y**2)**2 )

def calc_v(x,y):
    return V0*( -2*x*y/(x**2 + y**2)**2 )

fig, ax = plt.subplots()

x = np.linspace(-4.0, 4.0, 10)
y = np.linspace(0.0, 2.0, 5)
X, Y = np.meshgrid(x, y)
UXY = calc_u(X, Y)
VXY = calc_v(X, Y)

# Modify UXY and VXY if x and y is within the cylinder
for i in range(len(x)):
    for j in range(len(y)):
        if x[i]**2 + y[j]**2 <= 1.0:
            UXY[j,i] = 0.0
            VXY[j,i] = 0.0

ax.quiver(X, Y, UXY, VXY, width=3e-3)

x = np.linspace(-4.0, 4.0, 200)
y = np.linspace(0.0, 2.0, 200)
X, Y = np.meshgrid(x, y)
ϕ = calc_phi(X, Y)
ψ = calc_psi(X, Y)

# Modify ϕ and ψ if x and y is within the cylinder
for i in range(len(x)):
    for j in range(len(y)):
        if x[i]**2 + y[j]**2 <= 1.0:
            ϕ[j,i] = 0.0
            ψ[j,i] = 0.0

cs_phi = ax.contour(X, Y, ϕ, levels=8, colors="red")
cs_psi = ax.contour(X, Y, ψ, levels=5, colors="blue")
ax.clabel(cs_psi, inline=True, fontsize=10)
ax.clabel(cs_phi, inline=True, fontsize=10)

ax.grid(True)
#ax.set_xlim(-0.1, 6.1)
#ax.set_ylim(-0.1, 6.1)
ax.set_aspect("equal")

plt.savefig("IMG_Yang_example_8_4.png", dpi=150)
plt.show()
