from langchain_mistralai import ChatMistralAI
import streamlit as st


def create_llm():

    model = ChatMistralAI(
        model="mistral-small-latest",
        api_key=st.secrets["MISTRAL_API_KEY"]
    )

    return model