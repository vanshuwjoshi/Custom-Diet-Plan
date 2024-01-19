import streamlit as st
from bmr import get_bmr
from maintenance_calories import get_maintenance_calories
from required_calories import get_required_calories
from openai_api_response import get_openai_response


st.title("Get Your Custom Diet Plan")

col1, col2 = st.columns(2)


with st.form("calorie_form"):
    name = col1.text_input("Your name", key="name")
    age = col1.number_input("Your age", 0, 100, key="age")
    current_weight = col1.number_input(
        "Your current weight(in Kg)", 10, 200, key="current_weight"
    )
    current_height = col1.number_input(
        "Your current height(in cm)", 100, 250, key="current_height"
    )
    desired_weight = col1.number_input(
        "Your desired weight(in Kg)", 10, 200, key="desired_weight"
    )
    gender = col1.selectbox("Your gender", ["Male", "Female"], key="gender")
    activity_level = col1.selectbox(
        "Your activity level",
        ["Sedentary", "Moderately active", "Highly active", "Extremely active"],
        key="activity_level",
    )
    dietry = col1.selectbox(
        "Your dietry restrictions",
        ["Vegan", "Vegetarian", "Non-vegetarians"],
        key="dietry_restrictions",
    )

if col1.button("Calculate"):
    bmr = get_bmr(current_weight, current_height, age, gender)
    maintenance_calories = get_maintenance_calories(bmr, activity_level)
    required_calories = get_required_calories(
        maintenance_calories, current_weight, desired_weight
    )
    col2.write("Hi " + name + "!")
    col2.write("Your maintenance calories are: " + str(round(maintenance_calories)))
    col2.write("Your required calories are: " + str(round(required_calories)))
    
    response = get_openai_response(age, gender, required_calories, dietry)
    col2.write("Here is your custom meal plan:")
    col2.write("Breakfast: "+response.get("meal1"))
    col2.write("Mid-day snack: "+response.get("meal2"))
    col2.write("Lunch: "+response.get("meal3"))
    col2.write("Evening snack: "+response.get("meal4"))
    col2.write("Dinner: "+response.get("meal5"))
