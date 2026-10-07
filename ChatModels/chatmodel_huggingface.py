from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
  repo_id="zai-org/GLM-5.3",
  task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result=model.invoke("What is the capital of India", max_tokens=20,temperature=1)

print(result.content)