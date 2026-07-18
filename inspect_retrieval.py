from faiss_store import load_vector_store


def main():

    vector_store = load_vector_store()

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        docs_with_scores = vector_store.similarity_search_with_score(
            question,
            k=4
        )

        print("\n" + "=" * 100)

        for i, (doc, score) in enumerate(docs_with_scores, 1):

            print(f"\nResult {i}")
            print("-" * 100)
            print(f"Score    : {score:.4f}")
            print(f"Document : {doc.metadata.get('document_name')}")
            print(f"Category : {doc.metadata.get('category')}")
            print()
            print(doc.page_content[:600])

        print("\n" + "=" * 100)


if __name__ == "__main__":
    main()