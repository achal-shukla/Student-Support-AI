from rag import load_documents, split_documents
from faiss_store import create_vector_store


def main():

    print("Loading PDFs...")
    docs = load_documents()
    print(f"Loaded {len(docs)} pages.")

    print("\nSplitting documents...")
    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks.")

    print("\nCreating FAISS index...")
    create_vector_store(chunks)

    print("\n✅ Vector Store created successfully!")


if __name__ == "__main__":
    main()