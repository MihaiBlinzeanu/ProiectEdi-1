#!/usr/bin/env python3
"""RAG pipeline: search + Llama 3.3 70B (NVIDIA NIM) -> răspuns cu citări."""
import sys
sys.stdout.reconfigure(encoding="utf-8")

import os
import pickle
import numpy as np
import faiss
from nim_client import nim_embed, nim_chat

VECTOR_DIR = "vectors"

index = faiss.read_index(os.path.join(VECTOR_DIR, "faiss.index"))
with open(os.path.join(VECTOR_DIR, "chunks.pkl"), "rb") as f:
    all_chunks = pickle.load(f)
with open(os.path.join(VECTOR_DIR, "metadata.pkl"), "rb") as f:
    all_metadata = pickle.load(f)

SYSTEM_PROMPT = """Ești un asistent academic specializat în Automatică și Informatică Aplicată.
Răspunzi pe baza fragmentelor din cursuri furnizate mai jos.
Dacă informația nu este suficientă în fragmente, spune că nu știi.
Citează sursa pentru fiecare afirmație (numele cursului).
Răspunde în limba română."""


def search(query: str, top_k: int = 5) -> list:
    q_emb = np.array(nim_embed([f"query: {query}"], input_type="query"), dtype=np.float32)
    scores, indices = index.search(q_emb, top_k)
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


def generate(query: str, top_k: int = 5) -> str:
    results = search(query, top_k=top_k)
    context_parts = []
    for i, r in enumerate(results, 1):
        context_parts.append(
            f"[Fragment {i} - Sursa: {r['metadata']['source']}]\n{r['chunk']}"
        )
    context = "\n\n".join(context_parts)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Context:\n{context}\n\nÎntrebare: {query}"},
    ]

    answer = nim_chat(messages, temperature=0.3, max_tokens=1024)

    sources = list(set(r["metadata"]["source"] for r in results))
    answer += f"\n\n---\n**Surse:** {', '.join(sources)}"
    return answer


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/generate.py \"întrebare\"")
        sys.exit(1)
    query = sys.argv[1]
    answer = generate(query)
    print(answer)