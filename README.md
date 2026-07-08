# AIASSIST — Asistent RAG Local pentru Studenți

Sistem RAG (Retrieval-Augmented Generation) local care ingerează PDF-uri de curs și răspunde la întrebări cu citare sursă. Construit pentru practica de vară 2026 — Automatică și Informatică Aplicată, Anul III.

## Live Demo

**[proiect-edi.vercel.app](https://proiect-edi.vercel.app)**

## Capturi de ecran

![AIASSIST Interfață](Screenshot%20(474).png)
![Răspuns cu citări](Screenshot%20(475).png)

## Ce face

- **Ingest PDF**: Procesează automat PDF-uri de curs și le transformă în note structurate
- **Căutare semantică**: Găsește informații relevante folosind embeddings locali (FAISS + NVIDIA NIM)
- **Răspunsuri cu citări**: Oferă răspunsuri cu trimiteri exacte către sursa din curs
- **Anti-halucinație**: Dacă răspunsul nu e în surse, spune „nu am asta în surse"
- **100% local**: Funcționează offline, fără dependență de cloud

## Tech Stack

| Component | Tehnologie |
|-----------|------------|
| Parsare PDF | `pdfplumber` (text + metadate + poziționare cuvinte) |
| Chunking | 500 cuvinte, 100 overlap |
| Embeddings | `nvidia/nv-embed-v1` (4096d) via NVIDIA NIM |
| Vector DB | FAISS (IndexFlatIP, cosine similarity) |
| LLM | `meta/llama-3.3-70b-instruct` via NVIDIA NIM |
| Site | HTML/CSS/JS static (deploy pe Vercel) |

## Structura proiectului

```
ProiectEdi-1/
├── inbox/                    # PDF-uri de curs de procesat
│   ├── AutomatizareaCladirilor/
│   ├── Retelistica/
│   ├── Sisteme Automate/
│   └── TehnologiiWeb/
├── scripts/                  # Scripturi Python pentru pipeline
│   ├── ingest.py            # Parsează PDF-urile
│   ├── chunk_embed.py       # Creează embeddings
│   ├── search.py            # Căutare în vectori
│   ├── generate.py          # Generează răspunsuri
│   └── nim_client.py        # Client NVIDIA NIM
├── site/                     # Interfața web (statică)
├── concepts/                 # Notițe structurate
├── rag.py                   # CLI unificat
├── requirements.txt
└── vercel.json
```

## Instalare

```bash
# Clonează repository-ul
git clone https://github.com/MihaiBlinzeanu/ProiectEdi-1.git
cd ProiectEdi-1

# Instalează dependențele Python
pip install -r requirements.txt

# Configurează cheia NVIDIA NIM
echo "nvidia_api_key=nvapi-..." > .env
```

## Utilizare

### Pipeline de ingestie

```bash
# 1. Pune PDF-urile în inbox/
# 2. Rulează ingestia
python rag.py ingest

# 3. Creează embeddings
python rag.py reindex
```

### Interogare

```bash
# Răspuns complet cu citări
python rag.py ask "Ce este modelul OSI?"

# Căutare simplă
python rag.py search "rețea locală"
```

## Materii acoperite

- Automatizarea Clădirilor (9 cursuri)
- Retelistică (9 cursuri)
- Sisteme Automate
- Tehnologii Web (8 cursuri)

**Total**: 371 fragmente din 44 PDF-uri

## Echipă

- **Mihai Blînzeanu** — pipeline, note, search, site
- **Dorcea Eduard** — ingest, notes
- **Alin Gheorghe** — testing

## License

Proiect practică UTCB 2026.