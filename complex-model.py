"""
Problem: Optimal Energy Storage and Power Selling

A company owns an energy storage system with an initial energy capacity
of 500 energy units. The company can sell power at different prices
during 12 time periods (t = 0, 1, ..., 11).

The selling price varies by time period, and the storage system receives
additional energy through a charging schedule.

Decision variables:
    w[t] = energy/power sold during time period t
    s[t] = energy remaining in storage at the end of time period t

Objective:
    Maximize total revenue from selling energy.

    Maximize Z = sum(price[t] * w[t] for t in T)

Subject to:

1. Storage capacity constraint:
    s[t] <= 500                       for all t

2. Maximum power output constraint:
    w[t] <= 150                       for all t

# charge[t] is a predefined charging fraction in your model, while charge[t] * 500 converts that fraction 
# into an amount of energy. It is not automatically a real-world charging rate unless that is how the data
#  was defined.

3. Energy balance constraint for the first period:
    s[0] = 500 - w[0] + charge[0] * 500

4. Energy balance constraint for subsequent periods:
    s[t] = s[t-1] - w[t] + charge[t] * 500
                                         for t > 0

5. Non-negativity constraints:
    w[t] >= 0
    s[t] >= 0                          for all t

Question:
How much energy should the company sell during each time period to
maximize its total revenue while respecting the storage capacity,
power output limit, and charging schedule?
"""
import pyomo.environ as pyomo
import matplotlib.pyplot as plt

price_schedule={

  0: 0.5,
  1: 0.6,
  2: 1.0,
  3: 1.0,
  4: 0.9,
  5: 1.1,
  6: 1.8,
  7: 1.5,
  8: 0.9,
  9: 0.8,
  10: 0.7,          
  11: 0.6,
}

charge_schedule={

    0: 0.,
    1: 0.,
    2: 0.,
    3: 0.,
    4: 0.3,
    5: 0.15,
    6: 0.15,
    7: 0.05,
    8: 0.05,
    9: 0.05,
    10: 0.,          
    11: 0.,
}


model=pyomo.ConcreteModel()


# parameters and constant information
# number of time periods
model.nt=pyomo.Param(initialize=len(price_schedule),domain=pyomo.Integers) 

# set of time steps
model.T=pyomo.Set(initialize=range(model.nt()))

# sales price at each time step
model.price=pyomo.Param(model.T,initialize=price_schedule)

# power added from charging at each time step
model.charge=pyomo.Param(model.T,initialize=charge_schedule)


# initial/maximum storage inventory
model.S0=pyomo.Param(initialize=500.)

# maximum instantaneous power output
model.wmax=pyomo.Param(initialize=150.)



# --------variables-----------------

# power output

model.w=pyomo.Var(model.T,domain=pyomo.NonNegativeReals)

# energy stored
model.s= pyomo.Var(model.T,domain=pyomo.NonNegativeReals)


#---------------Objective function-----------------

def objective_func(model):
    # maximize revenue from selling power
    return sum(model.price[t]*model.w[t] for t in model.T)

# Here we define the objective function for the optimization model, which aims 
# to maximize the revenue generated from selling power at each time step based 
# on the price schedule and the power output variable.
model.objective=pyomo.Objective(rule=objective_func, sense=pyomo.maximize)


# constraints
def constr_store_capacity(model,t):
    return model.s[t] <= model.S0

# Here we define the constraint for storage capacity, ensuring that the stored energy at
#  any time step does not exceed the initial storage capacity.
model.const_store_capacity=pyomo.Constraint(model.T,rule=constr_store_capacity) 


def constr_power(model,t):
    return model.w[t] <= model.wmax

# Here we define the constraint for maximum power output, ensuring that the power output at any time step does not exceed the maximum instantaneous power output.
model.constr_power=pyomo.Constraint(model.T,rule=constr_power)


# energy balance on storage based on power consumed

# here multiplication by model.S0 because  

def constr_store_balance(model,t):
    if t==0:
        return model.s[t] == model.S0 - model.w[t] + model.charge[t]*model.S0
    else:
        return model.s[t] == model.s[t-1] - model.w[t] + model.charge[t]*model.S0


model.const_store_balance=pyomo.Constraint(model.T,rule=constr_store_balance)


# set up the solver
# I have my cbc solver in C folder
solver=pyomo.SolverFactory('cbc',executable=r"C:\Cbc\bin\cbc.exe")

# run the simulation
results=solver.solve(model,keepfiles=False,logfile="solve.log")



# Prinst and summarize the results

print(model.display())

print(f"Time\tPrice\tPower\tStorage")

for t in model.T:
    print(f"{t}\t{pyomo.value(model.price[t])}\t{pyomo.value(model.w[t])}\t{pyomo.value(model.s[t])}")



