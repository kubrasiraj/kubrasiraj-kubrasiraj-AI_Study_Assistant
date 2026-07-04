from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.embeddings import create_embeddings
from rag.vectorstore import create_vectorstore
from rag.retriever import create_retriever

def initialize_rag(file_path):


    docs=load_pdf(file_path)

    chunks=split_documents(docs)
    

    embeddings=create_embeddings()
    

    vectorstore=create_vectorstore(chunks,embeddings)
  

    retriever=create_retriever(vectorstore)

    return retriever
    





