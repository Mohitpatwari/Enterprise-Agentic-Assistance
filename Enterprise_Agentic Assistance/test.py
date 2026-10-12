import os, requests
from dotenv import load_dotenv

load_dotenv(override=True)
u = os.getenv("QDRANT_CLUSTER_ENDPOINT")
k = os.getenv("QDRANT_API_KEY")
print("URL:", repr(u))
print("Key length:", len(k or ""), "| ends:", (k or "")[-4:])
r = requests.get(u.rstrip("/") + "/collections", headers={"api-key": k}, timeout=15)
print("Status:", r.status_code)
print("Body:", r.text[:300])