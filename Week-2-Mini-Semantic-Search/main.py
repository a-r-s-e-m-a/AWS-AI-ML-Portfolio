import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
import re


# 1. Load FAQ data from CSV
def load_faqs():
    data = pd.read_csv("faqs.csv")

    print("FAQ data loaded successfully!")
    print("Number of FAQs:", len(data))

    return data


# 2. Clean the text
def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text


# 3. Split text into smaller chunks
def split_into_chunks(text, chunk_size=50, overlap=10):
    words = text.split()
    chunks = []

    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# 4. Prepare FAQ documents
def prepare_documents(data):
    documents = []
    metadatas = []
    ids = []

    for index, row in data.iterrows():

        question = clean_text(row["question"])
        answer = clean_text(row["answer"])

        text = "Question: " + question + " Answer: " + answer

        chunks = split_into_chunks(text)

        for chunk_number, chunk in enumerate(chunks):

            documents.append(chunk)

            metadatas.append({
                "question": question,
                "answer": answer
            })

            ids.append(str(index) + "_" + str(chunk_number))

    return documents, metadatas, ids


# 5. Create embeddings and store them in ChromaDB
def store_embeddings(documents, metadatas, ids, model):

    embeddings = model.encode(documents).tolist()

    client = chromadb.PersistentClient(path="chroma_db")

    collection = client.get_or_create_collection(
        name="faq_collection",
        metadata={"hnsw:space": "cosine"}
    )

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print("Embeddings stored successfully!")

    return collection


# 6. Search for similar FAQs
def search_faq(collection, model):

    query = input("\nEnter your question: ")

    query = clean_text(query)

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    print("\nTop 3 matching FAQs:")

    for i in range(len(results["ids"][0])):

        print("\nResult", i + 1)
        print("Question:", results["metadatas"][0][i]["question"])
        print("Answer:", results["metadatas"][0][i]["answer"])


# 7. Main program
def main():

    data = load_faqs()

    model = SentenceTransformer("all-MiniLM-L6-v2")

    documents, metadatas, ids = prepare_documents(data)

    collection = store_embeddings(
        documents,
        metadatas,
        ids,
        model
    )

    search_faq(collection, model)


main()