# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from sympy import * 

# %%
t = symbols("t", real=True, positive=True) 

# %% [markdown]
# # Soal 1

# %%
y = Function("y")(t)

# %%
y # already has t as independent variable

# %%
eqn1 = Equality( diff(y, t) + 5*y, 0 )
eqn1

# %%
dsolve( eqn1, y, ics={y.subs({t:0}) : 5} )

# %% [markdown]
# # Soal 2

# %%
y = Function("y")

# %%
eqn1 = Equality( diff(y(t), t, 2) + 2*diff(y(t), t), 0 )
eqn1

# %%
y(t).diff(t, 2)

# %%
y(t).diff(t, 1).subs({t: 0})

# %%
dsolve( eqn1, y(t) )

# %%
dsolve( eqn1, y(t), ics={ y(0): 1, y(t).diff(t, 1).subs({t: 0}) : 4} )

# %% [markdown]
# # Soal 3

# %%
t = symbols("t", negative=False)

# %%
Delta_t = DiracDelta(t)
Delta_t

# %%
lhs = diff(y(t), t, 1) + 2*y(t)
lhs

# %%
rhs = 3*diff(DiracDelta(t), t, 1) + 5*DiracDelta(t)
rhs

# %%
eqn1 = Equality( lhs, 0 )
eqn1

# %%
sol1 = dsolve( eqn1, y(t), ics={y(0): 1} )
sol1

# %% [markdown]
# Respon impulse:
# $$
# h(t)=b_{0}\delta(t)+\left[P(D)y_{n}(t)\right]u(t)
# $$

# %%
ynt = sol1.args[1]
ynt

# %%
pdynt = 3*diff( ynt, t ) + 5 * ynt
pdynt

# %%
Heaviside(t)

# %%
ht = 3*DiracDelta(t) + pdynt*Heaviside(t)
ht

# %%
diff(ht, t, 1) + 2*ht

# %%
3*diff(DiracDelta(t), t, 1) + 5*DiracDelta(t)

# %%
ht

# %%
ht

# %%
ht.subs({t: 0})

# %%
sympy.plot( ht, (t,1e-10,10) );

# %%
diff(ht, t, 1) + 

# %% [markdown]
# # Soal 3b

# %%
LHS = diff( y(t), t, 2 ) + 2*diff( y(t), t, 1 )

# %%
sol1 = dsolve( Equality(LHS, 0), ics={y(0): 0, y(t).diff(t,1).subs({t: 0}) : 1} )
sol1

# %%
ynt = sol1.args[1]
ynt

# %%
ht = diff( ynt, t, 1) + 4*ynt
ht

# %%
plot( ht, (t, 0, 10) )

# %% [markdown]
# # Soal 3c

# %%
LHS = diff(y(t), t, 2) + 2*diff(y(t), t, 1) + y(t)
LHS

# %%
y(t).diff(t,1).subs({t:0})

# %%
sol1 = dsolve( Equality(LHS, 0), ics={ y(0): 0, y(t).diff(t,1).subs({t:0}): 1 } )
sol1

# %%
ynt = sol1.args[1]
ynt

# %%
ht = diff(ynt, t, 1)
ht

# %%
factor(ht)

# %%
plot( ht, (t,0,2) )

# %% [markdown]
# ## Soal 4

# %% [markdown]
# Untuk suatu sistem LTIC dengan respon impuls satuan $h(t)=6e^{-t}u(t)$, tentukan respon sistem untuk input (a) $2u(t)$ dan (b) $3e^{-3t}u(t)$, dan (c) $e^{-t}u(t)$ (menggunakan konvolusi).

# %%
ht = 6*exp(-t)*Heaviside(t)
ht

# %%
τ = symbols("tau", real=True)

# %%
t

# %%
integrate( 2 * 6*exp(-(τ - t)), (τ, 0, t) )

# %%
integrate( 3*exp(-3*τ) * 6 * exp(-(τ - t)), (τ, 0, t) )

# %%
