# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:26:11 2020

@author: sergi
"""
from __future__ import division
from pyomo.environ import *
from pyomo.opt import SolverFactory
import numpy as np

#model
Model = ConcreteModel()

#sets
Model.tile = RangeSet(1,20)
Model.tubo = RangeSet(1,7)

#param
Model.blueprint = Param(Model.tubo,Model.tile,mutable=True)
for i in Model.tubo:
    for j in Model.tile:
        Model.blueprint[i,j] = 0

Model.blueprint[1,1]=1
Model.blueprint[1,5]=1
Model.blueprint[2,2]=1
Model.blueprint[2,3]=1
Model.blueprint[2,6]=1
Model.blueprint[2,7]=1
Model.blueprint[3,5]=1
Model.blueprint[3,9]=1
Model.blueprint[4,9]=1
Model.blueprint[4,10]=1
Model.blueprint[4,13]=1
Model.blueprint[4,14]=1
Model.blueprint[5,10]=1
Model.blueprint[5,11]=1
Model.blueprint[5,14]=1
Model.blueprint[5,15]=1
Model.blueprint[6,13]=1
Model.blueprint[6,17]=1
Model.blueprint[7,8]=1
Model.blueprint[7,12]=1
Model.blueprint[7,16]=1
Model.blueprint[7,19]=1
Model.blueprint[7,20]=1

#variable
Model.x = Var(Model.tile,domain=Binary)

#equations
Model.obj = Objective(expr = sum(Model.x[j] for j in Model.tile))
def tile_per_tube(Model,i):
    return sum(Model.blueprint[i,j]*Model.x[j] for j in Model.tile)==1
    
Model.res1 = Constraint(Model.tubo,rule=tile_per_tube)
#solver
SolverFactory("glpk").solve(Model)
Model.display()

