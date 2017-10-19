# Import necessary packages
from cvxopt import matrix, solvers

# Define Quadratic Objective
Q = 2*matrix([[2, 0.5], [0.5, 1]])
p = matrix([1.0, 1.0])

# Define Inequality Constraint
G = matrix([[-1.0, 0.0], [0.0, -1.0]])
h = matrix([0.0, 0.0])

# Define Equality Constraint
A = matrix([1.0, 1.0], (1, 2))
b = matrix(1.0)

# Find the minima using quadratic programming
sol = solvers.qp(Q, p, G, h, A, b)

print(sol['x'])
