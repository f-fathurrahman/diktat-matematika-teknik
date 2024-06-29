# %%
from sympy import *
init_printing()

# %%
s = symbols("s")
Y, Z = symbols("Y Z") # Laplace transformed functions
y0, z0 = symbols("y0 z0") # initial conditions

# %% [markdown]
# $$
# \begin{align*}
# \frac{\mathrm{d}y}{\mathrm{d} t} & = 2y - 3z \\
# \frac{\mathrm{d}z}{\mathrm{d} t} & = -2y + z
# \end{align*}
# $$
# Syarat awal: $y(0) = 8, z(0) = 3$

# %%
eq1 = Equality(s*Y - y0, 2*Y - 3*Z)
eq2 = Equality(s*Z - z0, -2*Y + Z)

# %%
eq1

# %%
eq2

# %%
sols = solve((eq1, eq2), (Y, Z))
sols

# %%
dict_num = {y0: 8, z0: 3}
Ys = sols[Y].subs(dict_num)
Zs = sols[Z].subs(dict_num)

# %%
Ys

# %% [markdown]
# Partial fraction expansion:

# %%
apart(Ys)

# %%
Zs

# %%
apart(Zs)

# %%
t = symbols("t", real=True, positive=True) # positive True to remove Heaviside factor
yt = inverse_laplace_transform(Ys, s, t)
zt = inverse_laplace_transform(Zs, s, t)

# %% [markdown]
# ## The solutions ($t > 0$, no Heaviside unit step function)

# %%
yt

# %%
zt

# %% [markdown]
# ## Checking the solutions

# %% [markdown]
# These two expression should be the same (to obey the 1st differential equation):

# %%
simplify( diff(yt, t) )

# %%
simplify( 2*yt - 3*zt )

# %% [markdown]
# These two expression should be the same (to obey the 2nd differential equation):

# %%
simplify( diff(zt, t) )

# %%
simplify( -2*yt + zt )

# %%
