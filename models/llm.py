from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os

load_dotenv()


def create_llm():

    model = ChatMistralAI(
        model="mistral-small-latest",
        api_key=os.getenv("MISTRAL_API_KEY")
    )

    return model