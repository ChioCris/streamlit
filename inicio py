import pulp


prob = pulp.LpProblem("Maximize_P", pulp.LpMaximize)

# Define variables
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Integer')

# Objective function
prob += 4 * x1 + 3 * x2 + 3 * x3, "Objective"

# Constraints
prob += 4 * x1 + 2 * x2 + x3 <= 10, "Constraint 1"
prob += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Constraint 2"
prob += 2 * x1 + x2 + 3 * x3 <= 7, "Constraint 3"

# Solve the problem
prob.solve()

# Print results
print("Status:", pulp.LpStatus[prob.status])
print("Optimal Solution to the problem:")
print(f"x1 = {x1.varValue}")
print(f"x2 = {x2.varValue}")
print(f"x3 = {x3.varValue}")
print("Objective = ", pulp.value(prob.objective))
