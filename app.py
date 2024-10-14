import streamlit as st

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit app title
st.title("Simple Calculator")

# Operation selection
operation = st.selectbox("Select an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Number inputs
num1 = st.number_input("Enter the first number:", format="%f")
num2 = st.number_input("Enter the second number:", format="%f")

# Calculate result
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.write(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.write(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.write(f"Result: {num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.write(f"Result: {num1} / {num2} = {result}")
