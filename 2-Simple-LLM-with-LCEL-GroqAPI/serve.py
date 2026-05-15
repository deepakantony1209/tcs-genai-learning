from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant", api_key=groq_api_key)
llm

## Prompt Template

system_prompt = "You are an expert transalator who is capable of transalating the sentence that user gives to {language}. You are proficient in converting the sentence that user gives to the requested language. The user can give whatever sentence they want in whichever language they want you need to translate it to the requested language.\n Make sure to only give the transalated sentence as output. The ouput you give should be accurate. Do not hallucinate, give the output response in perfect grammar and give accuate translation."

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{text}")
])

parser = StrOutputParser()

chain = prompt_template|llm|parser

## APP Definition

app = FastAPI(title="Langchain with Groq API",
              version="1.0.0",
              description="This is a simple application to demonstrate the use of Langchain with Groq API with runnable interfaces")

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
 