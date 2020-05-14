# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:13:25 2020

@author: sergi
"""

from __future__ import division
from pyomo.environ import *
from pyomo.opt import SolverFactory
import numpy as np

M = ConcreteModel()

#sets
M.d = RangeSet(1,7)

#parameters
tr = {1:17,2:13,3:15,4:19,5:14,6:16,7:11}
pos_trabajadores = np.ones((7,7))
for i in range(7):
        pos_trabajadores[i,i:i+2] = 0
pos_trabajadores[6,0] = 0
#variables
M.t = Var(M.d,domain=PositiveIntegers)
#equations
M.obj = Objective(expr=sum(M.t[i] for i in M.d))
M.res1 = ConstraintList()
    #col_vector = pos_trabajadores.transpose()
for i in range(7): 
   suma= 0
   for j in range(7):
       suma += pos_trabajadores[j,M.d[i+1]-1]*M.t[j+1]
   M.res1.add(suma >=tr[M.d[i+1]])

#solver
SolverFactory("glpk").solve(M)
M.display()
