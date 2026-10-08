from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
import os

load_dotenv()


hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN") 

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=hf_token
)

model=ChatHuggingFace(llm=llm)

template1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

template2=PromptTemplate(
    template="Write a 5 line summary on the following text ./n  {text}",
    input_variables=["topic"]
)

prompt1 = template1.invoke({"topic": "black hole"})


result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content  })

result1 = model.invoke(prompt2)

print(result1.content)


