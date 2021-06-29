#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sympy.interactive import printing 
printing.init_printing(use_latex=True)
from sympy import *
import sympy as sp

m1,y,g,phi,k,T,p,A,m0 =sp.symbols('m1,y,g,phi,k,T,p,A,m0', real =True)
m = sp.Function('m',real=True)(phi)
gleichung = Eq(y/(g*cos(phi))*(abs((-(2*k*T)/m0)+(p*cos(phi)*A/(y*sin(phi))))),m)
display(gleichung)
solve(y/(g*cos(phi))*(abs((-(2*k*T)/m0)+(p*cos(phi)*A/(y*sin(phi)))))-m,phi)


# In[ ]:





# In[ ]:




