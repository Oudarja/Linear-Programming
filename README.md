# Linear-Programming
A collection of linear programming and mathematical optimization problems implemented in Python using Pyomo and optimization solvers, with model formulation, constraints, objective functions, and solution analysis.
# Mathematical Optimization with Python and Pyomo

## Overview

This repository contains implementations of mathematical optimization problems using Python, Pyomo, and optimization solvers. It explores how real-world problems can be represented mathematically using decision variables, objective functions, and constraints, then solved computationally to obtain optimal solutions.

---

## Problem 1: Linear Programming

### Description

A company produces two products, Product 1 and Product 2. The objective is to determine the optimal production quantities that maximize total profit while satisfying a set of linear constraints.

### Objective Function

Maximize:

```
Z = x₁ + 10x₂
```

### Constraints

```
x₂ ≤ 10x₁ + 1
x₂ ≤ 0.2x₁ + 4
x₂ ≤ −0.2x₁ + 6
x₁, x₂ ≥ 0
```

### Goal

Find the optimal values of the decision variables x₁ and x₂ that maximize the objective function while satisfying all constraints.

---

## Problem 2: Optimization with Multiple Time Periods

### Description

This problem demonstrates optimization over multiple time periods using predefined parameters, decision variables, and time-dependent constraints. The model aims to maximize total revenue while respecting resource capacity, operational limits, and balance equations.

### Objective Function

Maximize:

```
Z = Σ (priceₜ · wₜ),   for all t ∈ T
```

### Constraints

- **Capacity constraints** limit the available stored resources.
- **Operational constraints** restrict the maximum output during each time period.
- **Balance equations** track changes in resource levels between consecutive periods.
- **Non-negativity constraints** ensure that decision variables remain non-negative.

### Goal

Determine the optimal output and resource levels for each time period to maximize the objective function while satisfying all model constraints.

---

## Technologies Used

- Python
- Pyomo
- CBC Optimization Solver
- Matplotlib

## Key Concepts

- Linear programming (LP)
- Objective function formulation
- Decision variables and constraints
- Resource allocation
- Multi-period optimization
- Mathematical modeling and solver integration

## Getting Started

1. Install Python.
2. Install the required packages:

   ```bash
   pip install pyomo matplotlib
   ```

3. Install the CBC optimization solver and ensure it is accessible to Pyomo.
4. Run the Python scripts to formulate and solve the optimization problems.

## Purpose

The purpose of this repository is to develop practical experience in mathematical optimization, computational modeling, and solving constrained optimization problems using Python.
