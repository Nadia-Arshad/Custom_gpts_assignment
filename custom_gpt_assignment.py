import streamlit as st
from meta_ai_api import MetaAI

llm = MetaAI()

user_input = input("Enter a question: ")

prompt = f"""You're a custom GPT that can answer questions about the weather in any country today and the date. 

          
          you just answer questions about weather, in case of any other questions, say: I don't know. 

          """

response = llm.prompt(prompt)
print(response["message"])
 
 