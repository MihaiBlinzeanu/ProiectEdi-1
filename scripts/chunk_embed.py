#!/usr/bin/env python3
"""Script pentru chunking text + embeddings NVIDIA NIM + FAISS din fișierele `processed/`."""
import sys
sys.stdout.reconfigure(encoding="utf-8")

import os
import json
import pickle
import numpy as np
from pathlib import Path
from tqdm import tqdm
import faiss
from nim_client import nim_embed

# Configurare
PROCESSED_DIR = "processed"
VECTOR_DIR = "vectors"
os.makedirs(VECTOR_DIR, exist_ok=True)

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
BATCH_SIZE = 32

all_chunks = []
all_metadata = []

for fname in sorted(os.listdir(PROCESSED_DIR)):
    if not fname.endswith(".json"):
        continue
    path = os.path.join(PROCESSED_DIR, fname)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    source = data["metadata"]["title"]
    full_text = "\n\n".join(p["text"] for p in data["pages"] if p.get("text"))
    if not full_text.strip():
        continue

    words = full_text.split()
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + CHUNK_SIZE])
        if chunk.strip():
            all_chunks.append(chunk)
            all_metadata.append({
                "source": source,
                "file": fname,
                "chunk_index": len(all_chunks),
                "word_range": (i, min(i + CHUNK_SIZE, len(words))),
            })
        i += CHUNK_SIZE - CHUNK_OVERLAP

print(f"[INFO] {len(all_chunks)} fragmente din {len(os.listdir(PROCESSED_DIR))} fișiere procesate")

print("[INFO] Generez embeddings via NVIDIA NIM...")
all_embeddings = []
for i in tqdm(range(0, len(all_chunks), BATCH_SIZE)):
    batch = all_chunks[i : i + BATCH_SIZE]
    embeds = nim_embed(batch, input_type="passage")
    all_embeddings.extend(embeds)

embeddings = np.array(all_embeddings, dtype=np.float32)
dim = embeddings.shape[1]

index = faiss.IndexFlatIP(dim)
index.add(embeddings)
print(f"[INFO] Index FAISS creat: {index.ntotal} vectori, dimensiune {dim}")

faiss.write_index(index, os.path.join(VECTOR_DIR, "faiss.index"))

with open(os.path.join(VECTOR_DIR, "chunks.pkl"), "wb") as f:
    pickle.dump(all_chunks, f)
with open(os.path.join(VECTOR_DIR, "metadata.pkl"), "wb") as f:
    pickle.dump(all_metadata, f)

print(f"[SUCCESS] Index și metadate salvate în `{VECTOR_DIR}/`\n"
      f"  - faiss.index ({index.ntotal} vectori)\n"
      f"  - chunks.pkl ({len(all_chunks)} fragmente)\n"
      f"  - metadata.pkl ({len(all_metadata)} metadate)")