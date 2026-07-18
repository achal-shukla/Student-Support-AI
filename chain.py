from faiss_store import load_vector_store
from llm import get_llm
from prompt import prompt
from config import COLLEGE_PLACEHOLDER
from responses import PREDEFINED_RESPONSES

vector_store = load_vector_store()

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.7
    }
)

llm = get_llm()


def ask_question(question):
    question_lower = question.strip().lower()

    if question_lower in PREDEFINED_RESPONSES:

     return {
        "answer": PREDEFINED_RESPONSES[question_lower],
        "sources": []
    }

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    context = context.replace(
        COLLEGE_PLACEHOLDER,
        "the college"
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    sources = []

    for doc in docs:

        name = doc.metadata.get("document_name")

        if name not in sources:
            sources.append(name)

    return {
        "answer": response.content,
        "sources": sources
    }