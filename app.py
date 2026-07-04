from rag.rag_pipeline import initialize_rag
from dotenv import load_dotenv
from models.llm import create_llm
from chat.chat import ask_question


"""file_path = input("Enter PDF path: ")

question = input("Ask your question: ")

mode = input("Enter mode: ")

retriever = initialize_rag(file_path)

model = create_llm()

answer = ask_question(
    question,
    mode,
    retriever,
    model
)

print(answer)"""


file_path = input("Enter PDF path: ")
retriever = initialize_rag(file_path)


model = create_llm()


question = input("Ask your question: ")
mode = input("Enter mode: ")


answer = ask_question(
    question,
    mode,
    retriever,
    model
)


print(answer)