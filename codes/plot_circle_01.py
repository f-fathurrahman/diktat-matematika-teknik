import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.0, 2*np.pi)
x = np.cos(t)
y = np.sin(t)

plt.clf()
plt.plot(x, y)
plt.axis("equal")
plt.savefig("IMG_circle_01.png", dpi=150)

