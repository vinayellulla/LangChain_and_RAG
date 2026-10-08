from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting topics about {topic}',
    input_variables=['topic']   
)

model = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.1
)

parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke('{Stomach}'))

# Visualize the Chain 

chain.get_graph().print_ascii()
