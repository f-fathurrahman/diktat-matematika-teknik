import numpy as np
import matplotlib.pyplot as plt

def u(x,y):
    return x**2 - y**2

def v(x,y):
    return 2*x*y

x = np.linspace(1e-4, 6.0, 200)
y = np.linspace(1e-4, 6.0, 200)
X, Y = np.meshgrid(x, y)

UXY = u(X,Y)
VXY = v(X,Y)

plt.clf()
#plt.contour(X, Y, UXY, levels=[1.0])
#plt.contour(X, Y, VXY, levels=[2.0])
plt.contour(X, Y, UXY, levels=10, colors="red")
plt.contour(X, Y, VXY, levels=10, colors="blue")
plt.grid(True)
plt.xlim(0.0, 6.0)
plt.ylim(0.0, 6.0)
plt.axis("equal")
plt.savefig("IMG_contour_01.png", dpi=150)
