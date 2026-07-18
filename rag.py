from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from text_cleaner import sanitize_text

from config import (
    DATA_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

def load_documents():
    """
    Load every PDF inside data/
    including all subfolders.
    """

    documents = []

    for pdf_path in DATA_DIR.rglob("*.pdf"):

        loader = PyPDFLoader(str(pdf_path))

        docs = loader.load()

        category = pdf_path.parent.name

        for doc in docs:
            doc.metadata["category"] = category
            doc.metadata["document_name"] = pdf_path.name
            doc.metadata.pop("source", None)

        documents.extend(docs)

    # Clean institution names
    for doc in documents:
        doc.page_content = sanitize_text(doc.page_content)

    return documents

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return splitter.split_documents(documents)