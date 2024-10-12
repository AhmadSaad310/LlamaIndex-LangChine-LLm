from langchain.embeddings.ollama import OllamaEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct

embeddings = OllamaEmbeddings(
    model="llama3.2"
)
input_text = ["LangChain is a framework for building applications using LLMs.",
               "Ollama provides easy access to various AI models.",
                "Generative AI is revolutionizing industries."]

x = embeddings.embed_documents(input_text)
print(x)

client = QdrantClient(url="http://localhost:6333")

points = [
    PointStruct(
        id=i + 1,  # Assign a unique ID to each point
        vector=embedding  # Convert embedding to a list for insertion
    )
    for i, embedding in enumerate(x)  # Loop through embeddings and create PointStruct
]
client.upsert(
    collection_name="New collection.",
    points=points  # Insert all points into the collection
)
