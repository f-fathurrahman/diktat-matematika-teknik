import numpy as np
import matplotlib.pyplot as plt

def calc_phi(x,y):
    return x**2 - y**2

def calc_psi(x,y):
    return 2*x*y


def calc_u(x,y):
    return 2*x

def calc_v(x,y):
    return -2*y

fig, ax = plt.subplots()

x = np.linspace(0.0, 6.0, 10)
y = np.linspace(0.0, 6.0, 10)
X, Y = np.meshgrid(x, y)
UXY = calc_u(X, Y)
VXY = calc_v(X, Y)
ax.quiver(X, Y, UXY, VXY)

x = np.linspace(1e-4, 6.0, 50)
y = np.linspace(1e-4, 6.0, 50)
X, Y = np.meshgrid(x, y)
ϕ = calc_phi(X, Y)
ψ = calc_psi(X, Y)

cs_phi = ax.contour(X, Y, ϕ, levels=8, colors="red")
cs_psi = ax.contour(X, Y, ψ, levels=8, colors="blue")
#ax.contour(X, Y, UXY, levels=10, colors="red")
#ax.contour(X, Y, VXY, levels=10, colors="blue")

ax.clabel(cs_psi, inline=True, fontsize=10)

ax.grid(True)
ax.set_xlim(-0.1, 6.1)
ax.set_ylim(-0.1, 6.1)
ax.set_aspect("equal", "box")

plt.savefig("IMG_Yang_example_8_3.png", dpi=150)
plt.show()
