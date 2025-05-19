import faiss
import pickle
from sentence_transformers import SentenceTransformer
from utils import chunk_text #, read_papers

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("data/faiss_index/index.faiss")

with open("data/faiss_index/chunks.pkl", "rb") as f:
    all_chunks = pickle.load(f)

def retrieve_chunks(query, k=5):
    embedding = model.encode([query])
    D, I = index.search(embedding, k)
    return "\n\n".join([all_chunks[i] for i in I[0]])