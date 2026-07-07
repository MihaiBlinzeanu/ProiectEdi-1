#!/usr/bin/env python3
"""Client partajat NVIDIA NIM — embeddings + chat completion."""
import sys
sys.stdout.reconfigure(encoding="utf-8")

import os
from dotenv import load_dotenv

load_dotenv()

NVIDIA_API_KEY = os.getenv("nvidia_api_key")
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"

HEADERS = {
    "Authorization": f"Bearer {NVIDIA_API_KEY}",
    "Content-Type": "application/json",
}

EMBEDDING_MODEL = "nvidia/nv-embed-v1"
LLM_MODEL = "meta/llama-3.3-70b-instruct"


def nim_embed(texts: list[str], input_type: str = "passage") -> list[list[float]]:
    import requests
    truncated = [t[:8000] if len(t) > 8000 else t for t in texts]
    resp = requests.post(
        f"{NVIDIA_BASE_URL}/embeddings",
        headers=HEADERS,
        json={
            "input": truncated,
            "model": EMBEDDING_MODEL,
            "input_type": input_type,
            "encoding_format": "float",
        },
        timeout=120,
    )
    if not resp.ok:
        detail = resp.text[:500]
        raise RuntimeError(f"NIM embeddings error {resp.status_code}: {detail}")
    data = resp.json()
    return [d["embedding"] for d in data["data"]]


def nim_chat(messages: list[dict], temperature: float = 0.3, max_tokens: int = 1024) -> str:
    import requests
    resp = requests.post(
        f"{NVIDIA_BASE_URL}/chat/completions",
        headers=HEADERS,
        json={
            "model": LLM_MODEL,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        },
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


if __name__ == "__main__":
    embed = nim_embed(["test embedding"], input_type="query")
    print(f"Embedding dim: {len(embed[0])}")
    answer = nim_chat([{"role": "user", "content": "Salut! Raspunde in romana."}])
    print(f"Chat: {answer}")