# import streamlit as st
# st.header("First App")
# name = st.text_input("Name")
# age = st.number_input("Age")
# st.write("Name:",name)
# st.write("Age:",age)
# st.code("inport streamlit as st('Hello world')")
# st.subheader("python code")

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
import streamlit as st
st.title("Calculator")
st.write("This is a simple calculator app")
a = st.number_input("Enter number")
b = st.number_input("Enter a number")
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])
if operation == "Add":
    st.write(add(a, b))
elif operation == "Subtract":
    st.write(sub(a, b))
elif operation == "Multiply":
    st.write(mul(a, b))
elif operation == "Divide":
    st.write(div(a, b))

