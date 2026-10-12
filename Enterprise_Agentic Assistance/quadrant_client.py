from qdrant_client import QdrantClient
import os

client = QdrantClient(
    url="https://3aad4aa2-ad8f-4709-adc7-a2534454f319.eu-west-1-0.aws.cloud.qdrant.io:6333",
    api_key=os.getenv("QDRANT_API_KEY")
)

# Get total count of vectors stored in your collection
info = client.get_collection(collection_name="enterprise_rag")
print(f"Total Vector Points Stored: {info.vectors_count}")