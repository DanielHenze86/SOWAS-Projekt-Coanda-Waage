#!/usr/bin/env python
# coding: utf-8

# In[10]:


from sympy.interactive import printing 
printing.init_printing(use_latex=True)
from sympy import *
import sympy as sp

x = sp.symbols('x')
m = sp.symbols('m')
v = sp.symbols('v')
a = sp.symbols('a')

f= sp.Function('f')(x)
diffeq=Eq(f.diff(x)+((a/(1+a*x)+m/(m*x-v)))*f,0)
display(diffeq)

dsolve(diffeq,f)


# In[ ]:




