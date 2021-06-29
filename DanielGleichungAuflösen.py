#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sympy.interactive import printing 
printing.init_printing(use_latex=True)
from sympy import *
import sympy as sp

a = sp.symbols('a')
v= sp.symbols('v')
m = sp.symbols('m')
g= sp.symbols('g')
y = sp.symbols('y')
pi = sp.symbols('pi')
phi = sp.symbols('phi')
s= sp.symbols('s')
rho= sp.symbols('rho')
R=sp.symbols('R')

gleichung = Eq((rho*v*pi*Pow(R,2))/(2*y)*(a*(v-sqrt((m*g*cos(phi))/(y)))-1)/(a*s*Pow(v,2)-a*s*v*sqrt((m*g*cos(phi))/(y))+(m*g*cos(phi))/(y)-a*v*(v-sqrt((m*g*cos(phi))/(y)))+s*(v-sqrt((m*g*cos(phi))/(y)))-v),tan(phi))
display(gleichung)
solve((rho*v*pi*Pow(R,2))/(2*y)*(a*(v-sqrt((m*g*cos(phi))/(y)))-1)/(a*s*Pow(v,2)-a*s*v*sqrt((m*g*cos(phi))/(y))+(m*g*cos(phi))/(y)-a*v*(v-sqrt((m*g*cos(phi))/(y)))+s*(v-sqrt((m*g*cos(phi))/(y)))-v),phi)


# In[ ]:




