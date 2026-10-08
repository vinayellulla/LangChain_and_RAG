from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Text_splitters/attention.pdf')

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

docs = loader.load()


result  = splitter.split_documents(docs)

print(result[2].page_content)