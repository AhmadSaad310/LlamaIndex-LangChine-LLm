from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance ,VectorParams

# Load a pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# texts to embed
texts = ["We haveing now a tasks",
          "And all this taskes speaking about Generativ AI"]

# Generate embeddings
embeddings =model.encode(texts)


# Print the shape of the embeddings instead of the full arrays
print("Embeddings shape:", embeddings.shape)
print("First embedding:", embeddings[0])

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="test_collection",
    vectors_config=VectorParams(size=384, distance=Distance.DOT),
)
client.create_collection(
    collection_name="Now every thing it is OK",
    vectors_config=VectorParams(size=384, distance=Distance.DOT),
)