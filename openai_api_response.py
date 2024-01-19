from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(temperature=0.0, openai_api_key=os.getenv("OPENAI_API_KEY"))

question_string = """ \
I am a {age} {gender}. \
My calorie goal for the day is {required_calories}. \ 
I am a {dietry}. I want to have 5 meals in a day. \ 
Create a meal plan using these details. \
Using these details answer the following question: \
meal1: What should be the breakfast and how many calories are in there? \
meal2: What should be the mid day snack and how many calories are in there? \
meal3: What should be the lunch and how many calories are in there? \
meal4: What should be the evening snack and how many calories are in there? \
meal5: What should be the dinner and how many calories are in there? \

{format_instructions}
"""

prompt_template = PromptTemplate(
    input_variables=["age", "gender", "required_calories", "dietry"],
    template=question_string,
)

meal1 = ResponseSchema(name="meal1", description="What should be the breakfast and how many calories are in there?")
meal2 = ResponseSchema(name="meal2", description="What should be the mid day snack and how many calories are in there?")
meal3 = ResponseSchema(name="meal3", description="What should be the lunch and how many calories are in there?")
meal4 = ResponseSchema(name="meal4", description="What should be the evening snack and how many calories are in there?")
meal5 = ResponseSchema(name="meal5", description="What should be the dinner and how many calories are in there?")

response_schema = [meal1, meal2, meal3, meal4, meal5]

output_parser = StructuredOutputParser.from_response_schemas(response_schema)
format_instructions = output_parser.get_format_instructions()

def get_openai_response(age,gender,required_calories,dietry):
    question = prompt_template.format(
        age=age,
        gender=gender,
        required_calories=required_calories,
        dietry=dietry,
        format_instructions=format_instructions
    )
    response = llm.invoke(question)
    response = output_parser.parse(response)
    return response
