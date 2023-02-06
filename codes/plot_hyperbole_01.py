import numpy as np
import matplotlib.pyplot as plt

t_grid = np.linspace(0.01, 2*np.pi-0.01, 100)
x_grid = 1/np.cos(t_grid)
y_grid = np.tan(t_grid)

x_min = np.min(x_grid)
x_max = np.max(x_grid)

y_min = np.min(y_grid)
y_max = np.max(y_grid)

plt.clf()
for i in range(len(t_grid)):
    x = x_grid[i]
    y = y_grid[i]
    plt.plot([x], [y], marker="o", color="blue")
    plt.axis("equal")
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.savefig("IMG_hyperbole_" + str(i) + ".png", dpi=150)
    print("i = ", i, " is done")
