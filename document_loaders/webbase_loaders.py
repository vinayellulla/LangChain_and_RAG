from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
# from bs4 import BeautifulSoup


model = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.1
)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text -\n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = "https://github.com/vinayellulla/LangChain_and_RAG"

loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0])

chain = prompt | model | parser 

print(chain.invoke({'question':'What is the product that we are talking about?','text':docs[0].page_content}))
