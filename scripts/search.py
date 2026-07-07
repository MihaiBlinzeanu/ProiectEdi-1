#!/usr/bin/env python3
"""Cautare semantica: NVIDIA NIM encode + FAISS search -> top-k chunks + metadata."""
import sys
sys.stdout.reconfigure(encoding="utf-8")

import os
import pickle
import numpy as np
import faiss
from nim_client import nim_embed

VECTOR_DIR = "vectors"

index = faiss.read_index(os.path.join(VECTOR_DIR, "faiss.index"))
with open(os.path.join(VECTOR_DIR, "chunks.pkl"), "rb") as f:
    all_chunks = pickle.load(f)
with open(os.path.join(VECTOR_DIR, "metadata.pkl"), "rb") as f:
    all_metadata = pickle.load(f)


def search(query: str, top_k: int = 5) -> list:
    query_embedding = np.array(nim_embed([f"query: {query}"], input_type="query"),
                               dtype=np.float32)
    scores, indices = index.search(query_embedding, top_k)
    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0:
            continue
        results.append({
            "score": float(score),
            "chunk": all_chunks[idx],
            "metadata": all_metadata[idx],
        })
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/search.py \"întrebare\"")
        sys.exit(1)
    query = sys.argv[1]
    results = search(query, top_k=5)
    print(f"Intrebare: {query}\n")
    for i, r in enumerate(results, 1):
        meta = r["metadata"]
        print(f"--- Fragment {i} (score: {r['score']:.3f}) ---")
        print(f"Sursa: {meta['source']}")
        print(f"Text: {r['chunk'][:300]}...")
        print()