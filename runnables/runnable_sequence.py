from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
load_dotenv()

model = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.1
)


prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

chain1 = RunnableSequence(prompt1,model,parser)

print(chain1.invoke({'topic': 'football'}))


chain = RunnableSequence(prompt1, model, parser, prompt2,model,parser)

print(chain.invoke({'topic': 'football'}))

