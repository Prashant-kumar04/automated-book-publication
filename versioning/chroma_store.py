import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(path=".chromadb")  # ✅ NEW STYLE
collection = client.get_or_create_collection(name="chapter_versions")

def store_version(id: str, content: str):
    collection.add(documents=[content], ids=[id])

def search_version(query: str):
    result = collection.query(query_texts=[query], n_results=2)
    return result

if __name__ == "__main__":
    with open("data/chapter_final.txt", "r", encoding="utf-8") as f:
        final = f.read()
    store_version("chapter1_final", final)
    print("Stored in ChromaDB.")
    print(search_version("grief and survival"))
