from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate 5 interesting topics about {topic}',
    input_variables=['topic']   
)

prompt2 = PromptTemplate(
    template='Generate 5 point summary from the following text \n {text}',
    input_variables=['text']   
)

model = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.1
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser 


result = chain.invoke({'topic' : 'Unemployment in India'})

print(result)

# Visualize the Chain 

# chain.get_graph().print_ascii()