from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

model = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.1
)

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

with open("document_loaders/cricket.txt", "r", encoding="utf-8") as f:
    text = f.read()

docs = [Document(page_content=text,metadata={"source":"document_loaders/cricket.txt"})]

print(type(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({"poem" : docs[0].page_content}))