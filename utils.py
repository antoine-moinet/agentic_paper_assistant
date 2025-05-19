import os
import faiss
import pickle
#import numpy as np
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader

def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def read_papers():
    # Load and chunk all papers
    all_chunks = []
    for filename in os.listdir("data/papers"):
        if filename.endswith(".pdf"):
            reader = PdfReader(os.path.join("data/papers", filename))
            text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
            chunks = chunk_text(text)
            all_chunks.extend(chunks)

    # Embed chunks
    model = SentenceTransformer("all-MiniLM-L6-v2")  
    embeddings = model.encode(all_chunks, convert_to_numpy=True).astype("float32")

    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)  # If there's only one embedding, make it 2D


    # Build FAISS index
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    # Create output directory if it doesn't exist
    os.makedirs("data/faiss_index", exist_ok=True)

    # Save FAISS index
    faiss.write_index(index, "data/faiss_index/index.faiss")

    # Save text chunks for retrieval
    with open("data/faiss_index/chunks.pkl", "wb") as f:
        pickle.dump(all_chunks, f)

    #print("✅ Index built and saved.")
    return