import streamlit as st
import pandas as pd

st.title("Diet Generating Application")

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

if col1.button("Calculate"):
    bmr = (10 * current_weight) + (6.25 * current_height) - (5 * age)
    if gender == "Male":
        bmr = bmr + 5
    else:
        bmr = bmr - 161
    maintenance_calories = bmr
    if activity_level == "Sedentary":
        maintenance_calories *= 1.2
    elif activity_level == "Moderately active":
        maintenance_calories *= 1.375
    elif activity_level == "Highly active":
        maintenance_calories *= 1.725
    else:
        maintenance_calories *= 1.9
    required_calories = maintenance_calories
    if desired_weight > current_weight:
        required_calories += 500
    elif desired_weight < current_weight:
        required_calories -= 500
    else:
        required_calories = maintenance_calories
    col2.write("Hi " + name + "!")
    col2.write("Your maintenance calories are: " + str(round(maintenance_calories)))
    col2.write("Your required calories are: " + str(round(required_calories)))
    col2.write(
        "** Keep in mind that this is just an estimate and your actual calorie needs may vary depending on your activity level, metabolism, and other factors. It is always best to consult with a healthcare professional or registered dietitian to determine a personalized calorie goal for your specific needs and goals."
    )

    dietry = col2.selectbox(
        "Your dietry restrictions",
        ["Vegan", "Vegetarian", "Non-vegetarians"],
        key="dietry_restrictions",
    )

    number_of_meals = col2.slider("Number of meals you want to eat in a day", 2, 7, 3)

    col2.button("Generate Diet Plan")


# with st.form("my_form"):
#     name = col1.text_input("Your name", key="name")
#     age = col1.number_input("Your age", 0, 100, key="age")
#     current_weight = col1.number_input(
#         "Your current weight(in Kg)", 10, 200, key="current_weight"
#     )
#     desired_weight = col1.number_input(
#         "Your desired weight(in Kg)", 10, 200, key="desired_weight"
#     )
#     gender = col1.selectbox("Your gender", ["Male", "Female"], key="gender")
#     dietry = col1.selectbox(
#         "Your dietry restrictions",
#         ["Vegan", "Vegetarian", "Non-vegetarians"],
#         key="dietry_restrictions",
#     )

# if col1.button("Generate"):
#     col2.write("Hi " + name + "!")
#     prompt_string = (
#         "You are a "
#         + str(age)
#         + " year old "
#         + gender
#         + ". Your current weight is "
#         + str(current_weight)
#         + " and your desired weight is "
#         + str(desired_weight)
#         + "."
#     )
#     col2.write(prompt_string)
#     col2.write("We will use this information to genrate your custom diet.")
