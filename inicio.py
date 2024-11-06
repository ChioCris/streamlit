import streamlit as st
import pulp

# Título de la aplicación
st.title("Problema de Optimización Lineal")

# Descripción del problema
st.write("""
Este es un ejemplo de un problema de optimización lineal que maximiza una función objetivo
sujeta a varias restricciones.
""")

# Definir el problema
prob = pulp.LpProblem("Maximize_P", pulp.LpMaximize)

# Definir las variables
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Integer')

# Función objetivo
prob += 4 * x1 + 3 * x2 + 3 * x3, "Objective"

# Restricciones
prob += 4 * x1 + 2 * x2 + x3 <= 10, "Constraint 1"
prob += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Constraint 2"
prob += 2 * x1 + x2 + 3 * x3 <= 7, "Constraint 3"

# Resolver el problema
prob.solve()

# Mostrar el estado de la solución
st.write("**Estado:**", pulp.LpStatus[prob.status])

# Mostrar los valores óptimos de las variables
st.write("**Solución Óptima:**")
st.write(f"x1 = {x1.varValue}")
st.write(f"x2 = {x2.varValue}")
st.write(f"x3 = {x3.varValue}")

# Mostrar el valor óptimo de la función objetivo
st.write("**Valor de la Función Objetivo:**", pulp.value(prob.objective))
