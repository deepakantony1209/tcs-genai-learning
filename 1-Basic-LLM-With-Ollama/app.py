## First OLLAMA GEN AI Application

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANCHAIN_PROJECT"] = os.getenv("LANCHAIN_PROJECT")
os.environ['LANGCHAIN_TRACING_V2'] = 'true'

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

## Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the questions asked"),
    ("user", "Question: {question}")

])

## Streamlit UI
st.title("Langchain with Gemma")
input_text = st.text_input("What do you have in your mind?")

llm = Ollama(model="gemma3n:latest")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)