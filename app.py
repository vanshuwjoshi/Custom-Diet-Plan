import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from bmr import get_bmr
from maintenance_calories import get_maintenance_calories
from required_calories import get_required_calories

load_dotenv()

llm = OpenAI(temperature=0.0, openai_api_key=os.getenv("OPENAI_API_KEY"))


def get_openai_response(question):
    response = llm.invoke(question)
    return response


question_string = "I am a {age} {gender}. My calorie goal for the day is {required_calories}. I am a {dietry}. I want to have {number_of_meals} meals in a day. Could you please suggest me a meal plan for today?"

prompt_template = PromptTemplate(
    input_variables=["age", "gender", "required_calories", "dietry", "number_of_meals"],
    template=question_string,
)

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

    number_of_meals = col1.slider("Number of meals you want to eat in a day", 2, 7, 3)

if col1.button("Calculate"):
    bmr = get_bmr(current_weight, current_height, age, gender)
    maintenance_calories = get_maintenance_calories(bmr, activity_level)
    required_calories = get_required_calories(
        maintenance_calories, current_weight, desired_weight
    )
    col2.write("Hi " + name + "!")
    col2.write("Your maintenance calories are: " + str(round(maintenance_calories)))
    col2.write("Your required calories are: " + str(round(required_calories)))
    col2.write(
        "** Keep in mind that this is just an estimate and your actual calorie needs may vary depending on your activity level, metabolism, and other factors. It is always best to consult with a healthcare professional or registered dietitian to determine a personalized calorie goal for your specific needs and goals."
    )
    question = prompt_template.format(
        age=age,
        gender=gender,
        required_calories=required_calories,
        dietry=dietry,
        number_of_meals=number_of_meals,
    )
    response = get_openai_response(question=question)
    col2.write(response)
