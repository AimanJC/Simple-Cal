import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit app title
st.title("Cool Scientific Calculator")

# Sidebar for scientific operations
operation = st.sidebar.selectbox(
    "Choose an operation", 
    ("Basic", "Trigonometric", "Logarithmic", "Exponential", "Graph")
)

st.write("### Enter Values:")

# Input fields
num1 = st.number_input("Enter the first number:", format="%f")
num2 = st.number_input("Enter the second number (if needed):", format="%f", value=0.0)

# Calculate based on selected operation
if operation == "Basic":
    basic_operation = st.selectbox("Select basic operation:", ("Add", "Subtract", "Multiply", "Divide"))
    if basic_operation == "Add":
        result = num1 + num2
        st.write(f"Result: {num1} + {num2} = {result}")
    elif basic_operation == "Subtract":
        result = num1 - num2
        st.write(f"Result: {num1} - {num2} = {result}")
    elif basic_operation == "Multiply":
        result = num1 * num2
        st.write(f"Result: {num1} * {num2} = {result}")
    elif basic_operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Error! Division by zero."
        st.write(f"Result: {num1} / {num2} = {result}")

elif operation == "Trigonometric":
    trig_operation = st.selectbox("Select trigonometric function:", ("sin", "cos", "tan"))
    angle = st.number_input("Enter angle in degrees:", format="%f")
    radians = np.radians(angle)
    if trig_operation == "sin":
        result = np.sin(radians)
    elif trig_operation == "cos":
        result = np.cos(radians)
    elif trig_operation == "tan":
        result = np.tan(radians)
    st.write(f"Result: {trig_operation}({angle}) = {result}")

elif operation == "Logarithmic":
    log_operation = st.selectbox("Select logarithmic function:", ("log", "log10", "log2"))
    if log_operation == "log":
        result = np.log(num1) if num1 > 0 else "Error! Logarithm only defined for positive numbers."
    elif log_operation == "log10":
        result = np.log10(num1) if num1 > 0 else "Error! Logarithm only defined for positive numbers."
    elif log_operation == "log2":
        result = np.log2(num1) if num1 > 0 else "Error! Logarithm only defined for positive numbers."
    st.write(f"Result: {log_operation}({num1}) = {result}")

elif operation == "Exponential":
    exp_operation = st.selectbox("Select exponential function:", ("exp", "pow"))
    if exp_operation == "exp":
        result = np.exp(num1)
    elif exp_operation == "pow":
        result = np.power(num1, num2)
    st.write(f"Result: {exp_operation}({num1}, {num2}) = {result}")

elif operation == "Graph":
    graph_type = st.selectbox("Select function type to plot:", ("Linear", "Quadratic", "Sine", "Cosine", "Exponential"))
    x_values = np.linspace(-10, 10, 400)
    
    if graph_type == "Linear":
        y_values = num1 * x_values + num2
    elif graph_type == "Quadratic":
        y_values = num1 * x_values**2 + num2
    elif graph_type == "Sine":
        y_values = np.sin(num1 * x_values)
    elif graph_type == "Cosine":
        y_values = np.cos(num1 * x_values)
    elif graph_type == "Exponential":
        y_values = num1 * np.exp(x_values)
    
    plt.figure(figsize=(8, 4))
    plt.plot(x_values, y_values)
    plt.title(f"{graph_type} Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    st.pyplot(plt)
