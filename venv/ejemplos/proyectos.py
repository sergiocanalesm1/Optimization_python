# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:44:26 2020

@author: sergi
"""

from __future__ import division
from pyomo.environ import *
from pyomo.opt import SolverFactory



# M = model
M = ConcreteModel()

# Sets and Parameters

#M.valor=[2, 5, 4, 2, 6, 3, 1, 4]

numProyectos=8

M.p=RangeSet(1, numProyectos)

M.valor=Param(M.p, mutable=True)

for i in M.p:
    M.valor[i]=2  

M.valor[1]=2
M.valor[2]=5
M.valor[3]=4
M.valor[4]=2
M.valor[5]=6
M.valor[6]=3
M.valor[7]=1
M.valor[8]=4

#a=M.valor.__dict__
#b=dir(M.valor._data[1])
#c=M.valor._data[1].value
     
#for i in M.p:
#    print(M.valor._data[i].value)
    

# Variables
M.x = Var(M.p, domain=Binary)

# Objective Function
M.obj = Objective(expr = sum(M.x[i]*M.valor[i] for i in M.p), sense=maximize)

# Constraints
#def res1(M):
#    return 
M.res1 = Constraint(expr = sum(M.x[i] for i in M.p) == 2)

# Applying the solver
SolverFactory('glpk').solve(M)

M.display()
