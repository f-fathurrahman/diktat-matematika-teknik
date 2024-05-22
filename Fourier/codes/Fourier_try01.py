# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import matplotlib.pyplot as plt

# %%
import matplotlib_inline
matplotlib_inline.backend_inline.set_matplotlib_formats("svg")

# %%
import matplotlib
matplotlib.style.use("dark_background")

# %%
import numpy as np

# %% [markdown]
# $$
# f(x) = \frac{4k}{\pi}\sum_{n=1}\frac{1}{2n-1}\sin\left(2n-1\right)x
# $$

# %%
NptsPlot = 500
xmin = 0.0
xmax = 2*np.pi
xgrid = np.linspace(xmin, xmax, NptsPlot)
y = np.zeros(NptsPlot)

Nterms = 100
k = 1.0
prefactor = 4*k/np.pi
for n in range(1,Nterms+1):
    y += 1/(2*n-1) * np.sin( (2*n - 1)*xgrid )
y *= prefactor

plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
plt.plot(xgrid, y);

# %%
plt.
