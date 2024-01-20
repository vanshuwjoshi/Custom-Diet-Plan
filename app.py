import streamlit as st
from bmr import get_bmr
from maintenance_calories import get_maintenance_calories
from required_calories import get_required_calories
from openai_api_response import get_openai_response

st.title("Get Your Custom Diet Plan")

with st.form("calorie_form"):
    name = st.sidebar.text_input("Your name", key="name")
    age = st.sidebar.number_input("Your age", 0, 100, key="age")
    current_weight = st.sidebar.number_input(
        "Your current weight(in Kg)", 10, 200, key="current_weight"
    )
    desired_weight = st.sidebar.number_input(
        "Your desired weight(in Kg)", 10, 200, key="desired_weight"
    )
    current_height = st.sidebar.number_input(
        "Your current height(in cm)", 100, 250, key="current_height"
    )
    gender = st.sidebar.selectbox("Your gender", ["Male", "Female"], key="gender")
    activity_level = st.sidebar.selectbox(
        "Your activity level",
        ["Sedentary", "Moderately active", "Highly active", "Extremely active"],
        key="activity_level",
    )
    dietary = st.sidebar.selectbox(
        "Your dietary restrictions",
        ["Vegan", "Vegetarian", "Non-vegetarians"],
        key="dietary_restrictions",
    )

if st.sidebar.button("Generate diet"):
    bmr = get_bmr(current_weight, current_height, age, gender)
    maintenance_calories = get_maintenance_calories(bmr, activity_level)
    required_calories = get_required_calories(
        maintenance_calories, current_weight, desired_weight
    )
    st.header("Hi " + name + "!")
    st.write("Your maintenance calories are: " + str(round(maintenance_calories)))
    st.write("Your required calories are: " + str(round(required_calories)))

    response = get_openai_response(age, gender, required_calories, dietary)
    st.header("Here is your custom meal plan:")
    st.subheader("Breakfast:")
    st.write(response.get("meal1"))
    st.subheader("Mid-day snack:")
    st.write(response.get("meal2"))
    st.subheader("Lunch:")
    st.write(response.get("meal3"))
    st.subheader("Evening snack:")
    st.write(response.get("meal4"))
    st.subheader("Dinner:")
    st.write(response.get("meal5"))
