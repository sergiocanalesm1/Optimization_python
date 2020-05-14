# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:13:11 2020

@author: sergi
"""

from __future__ import division
from pyomo.environ import *
from pyomo.opt import SolverFactory

M = ConcreteModel()

#sets
M.c = RangeSet(1,8)
#parameters
tipo = {1:["blues rock"],
      2:["rock and roll"],
      3:["blues rock"],
      4:["rock and roll"],
      5:["blues rock"],
      6:["rock and roll"],
      7:[],
      8:["blues rock","rock and roll"]          
      }
duracion ={1:4,
          2:5,
          3:3,
          4:2,
          5:4,
          6:3,
          7:5,
          8:4
          }
#variables
M.x1 = Var(M.c,domain=Binary)
M.x2 = Var(M.c,domain=Binary)
#equations
M.obj = Objective(expr=sum(M.x1[i]*duracion[i] + M.x2[i]*duracion[i] for i in M.c) )
M.d1down = Constraint(expr=sum((M.x1[i]*duracion[i] for i in M.c)) >= 14)
M.d1up = Constraint(expr=sum((M.x1[i]*duracion[i] for i in M.c)) <= 16)
M.d2down = Constraint(expr=sum((M.x2[i]*duracion[i] for i in M.c)) >= 14)
M.d2up = Constraint(expr=sum((M.x2[i]*duracion[i] for i in M.c)) <= 16)
M.res1 = Constraint(expr=sum(M.x1[i] for i in M.c if "blues rock" in tipo[i])==2)
M.res2 = Constraint(expr=sum(M.x2[i] for i in M.c if "blues rock" in tipo[i])==2)
M.res3 = Constraint(expr=sum(M.x1[i] for i in M.c if "rock and roll" in tipo[i]) >= 3)
M.res4 = Constraint(expr=M.x1[1] + M.x1[5] <=1)
M.res5 = Constraint(expr=M.x1[2]+M.x1[4] <= M.x2[1] + 1)
def no_repeat(M,i):
    return M.x1[i] + M.x2[i] <= 1
M.res6 = Constraint(M.c,rule=no_repeat)
#solver
SolverFactory("glpk").solve(M)
M.display()
