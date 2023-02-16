import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
# cm: colormap

fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={"projection": "3d"})

x = np.linspace(-5.0, 5.0, 100)
y = np.linspace(-5.0, 5.0, 100)

X, Y = np.meshgrid(x, y)

Z = X + 1j*Y

fZ = np.conj(Z)*Z**2

surf1 = ax1.plot_surface(X, Y, np.real(fZ), cmap=cm.coolwarm, linewidth=0)
ax1.set_title("Real part")

surf2 = ax2.plot_surface(X, Y, np.imag(fZ), cmap=cm.coolwarm, linewidth=0)
ax2.set_title("Imag part")

fig.suptitle(r"Plot of fZ")
plt.savefig("IMG_cZZ2.png", dpi=150)
plt.show()
