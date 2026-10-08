from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('document_loaders/attention.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)

print("--------------------------------")

print(docs[1].metadata)

