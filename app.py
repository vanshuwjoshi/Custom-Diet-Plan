import streamlit as st
import pandas as pd


st.title("Diet Generating Application")

col1, col2 = st.columns(2)
with st.form("my_form"):
    name = col1.text_input("Your name", key="name")
    age = col1.number_input("Your age", 0, 100, key="age")
    current_weight = col1.number_input(
        "Your current weight(in Kg)", 10, 200, key="current_weight"
    )
    desired_weight = col1.number_input(
        "Your desired weight(in Kg)", 10, 200, key="desired_weight"
    )
    gender = col1.selectbox("Your gender", ["Male", "Female"], key="gender")
    dietry = col1.selectbox(
        "Your dietry restrictions",
        ["Vegan", "Vegetarian", "Non-vegetarians"],
        key="dietry_restrictions",
    )

if col1.button("Generate"):
    col2.write("Hi " + name + "!")
    prompt_string = (
        "You are a "
        + str(age)
        + " year old "
        + gender
        + ". Your current weight is "
        + str(current_weight)
        + " and your desired weight is "
        + str(desired_weight)
        + "."
    )
    col2.write(prompt_string)
    col2.write("We will use this information to genrate your custom diet.")
