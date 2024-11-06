import streamlit as st
import pulp

def main():
    st.title("Problema de Optimización con PuLP")
    st.write("""
    ### Problema de Optimización Lineal
    Minimizar: C(x, y) = x - y  
    Sujeto a:  
    - 3x + 4y ≤ 6  
    - x - y ≤ 1  
    - x, y ≥ 0
    """)

    prob = pulp.LpProblem("Minimize_C", pulp.LpMinimize)
    x = pulp.LpVariable('x', lowBound=0)
    y = pulp.LpVariable('y', lowBound=0)

    prob += x - y, "Objective"

    prob += 3 * x + 4 * y <= 6, "Constraint 1"
    prob += x - y <= 1, "Constraint 2"
    prob.solve()
    st.write("**Solución Relajada (No entera):**")
    st.write(f"x = {x.varValue}")
    st.write(f"y = {y.varValue}")
    st.write("Valor de la función objetivo =", pulp.value(prob.objective))
    if x.varValue.is_integer() and y.varValue.is_integer():
        st.write("La solución es entera. No se necesitan planos de corte adicionales.")
    else:
        st.write("La solución no es entera. Se necesitarían planos de corte adicionales (no implementados en este ejemplo).")
if __name__ == "__main__":
    main()
