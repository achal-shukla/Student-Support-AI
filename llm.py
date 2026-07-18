from langchain_cohere import ChatCohere

from config import COHERE_API_KEY


def get_llm():

    llm = ChatCohere(
        cohere_api_key=COHERE_API_KEY,
        model="command-a-03-2025",
        temperature=0
    )

    return llm