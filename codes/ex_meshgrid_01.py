import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
# cm: colormap

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

#x = np.array([0.0, 1.0, 2.0])
#y = np.array([3.0, 5.0, 6.0, 7.0])

x = np.linspace(-5.0, 5.0, 100)
y = np.linspace(-5.0, 5.0, 100)

X, Y = np.meshgrid(x, y)

Z = X + 1j*Y

#W = Z**2 # evaluate a complex-valued function
fZ = np.log(Z)


surf1 = ax.plot_surface(X, Y, np.real(fZ), cmap=cm.coolwarm, linewidth=0)
plt.savefig("IMG_01_real.png", dpi=150)

ax.cla()
surf1 = ax.plot_surface(X, Y, np.imag(fZ), cmap=cm.coolwarm, linewidth=0)
plt.savefig("IMG_01_imag.png", dpi=150)

