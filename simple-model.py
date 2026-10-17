"""
A company produces two products, Product 1 and Product 2. Let x1 and x2
represent the quantities produced.

The company wants to maximize its total profit, represented by:

    Maximize Z = x1 + 10*x2

Subject to the following constraints:

    x2 <= 10*x1 + 1
    x2 <= 0.2*x1 + 4
    x2 <= -0.2*x1 + 6

Non-negativity constraints:

    x1 >= 0
    x2 >= 0

Question:
How many units of each product should the company produce to maximize
its total profit?
"""

import pyomo.environ as pyomo

model=pyomo.ConcreteModel()

# means x1 >= 0
model.x1=pyomo.Var(domain=pyomo.NonNegativeReals)
# means x2 >= 0
model.x2=pyomo.Var(domain=pyomo.NonNegativeReals)

# It is a list of constraints, so we can add as many constraints
#  as we want
model.c=pyomo.ConstraintList()

model.c.add(model.x1*10+1>=model.x2)

model.c.add(model.x1*(0.2)+4 >= model.x2)

model.c.add(model.x1*(-0.2)+6 >= model.x2)

# Objective function
# It is a function that takes the model as input and returns 
# the value of the objective function
model.objective = pyomo.Objective(rule=lambda model: model.x1+model.x2*10, sense=pyomo.maximize)
            
# solver

solver=pyomo.SolverFactory('cbc',executable=r"C:\Cbc\bin\cbc.exe")

result=solver.solve(model)

print(result)



print("x1=",model.x1())
print("x2=",model.x2())




