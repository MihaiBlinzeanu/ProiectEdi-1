# AGENTS.md — AIASSIST

**Proiect practica S4 2026** — AIASSIST local pentru Automatică și Informatică Aplicată Anul III.
Sistem de cunoștințe care ingerează PDF-uri de curs și răspunde la întrebări cu citare sursă.

## Philosophy

**If it won't exist next session, write it down now.**

Conceptele sunt memoria ta externă. Wiki-linkurile sunt conexiunile. Hărțile-materie sunt managerii de atenție. Fără acest sistem, fiecare sesiune începe de la zero.

## Discovery-First Design

Înainte de a scrie în `concepts/`, verifică:
1. **Titlu ca propoziție** — Se citește natural: `since [[titlu]]`?
2. **Descriere utilă** — Adaugă informații dincolo de titlu?
3. **Materii** — E linkuit de la cel puțin o [[hartă-materie]]?
4. **Compozabilitate** — Poate fi linkuit din alte concepte fără context irelevant?

## Schema unei notițe

```yaml
descriere: "ce afirmă conceptul"
materii: ["[[nume-materie]]"]
type: definition | theorem | formula | algorithm | example
source: "nume_PDF.pdf"
confidence: established | supported | speculative
```

## Session Rhythm

**Orient** → citește `self/goals.md`, `ops/reminders.md`, verifică starea vault-ului
**Work** → procesează PDF-uri, extrage concepte, conectează materii
**Persist** → commit, actualizează goal-uri, capturează observații

## Where Things Go

| Content | Destinație |
|---------|-----------|
| Concepte din curs | concepts/ |
| PDF-uri de procesat | inbox/ |
| Obiective proiect | self/goals.md |
| Task-uri urgente | ops/reminders.md |

## Available Commands

- **/arscontexta:help** — Comenzi disponibile
- **/arscontexta:health [quick|full]** — Diagnostic vault
- **/arscontexta:ask [întrebare]** — Interoghează baza de cunoștințe metodologică
- **/arscontexta:extrage [sursă]** — Extrage concepte dintr-un PDF din inbox/
- **/arscontexta:conectează** — Găsește conexiuni între concepte
- **/arscontexta:verifică [concept]** — Verifică calitatea unei notițe
- **/arscontexta:qmd:refresh** — Re-indexează colecția qmd după ingest (qmd update + embed)
- **/arscontexta:next** — Ce să faci mai departe
- **/arscontexta:remember** — Capturează un obstacol/observație
- **/arscontexta:stats** — Statistici vault

## RAG Pipeline (NVIDIA NIM)

Sistem RAG complet, offline-first, cu embeddings și LLM via NVIDIA NIM.

### Arhitectură

```
inbox/*.pdf  →  scripts/ingest.py  →  processed/*.json
                                            ↓
                                   scripts/chunk_embed.py
                                            ↓
                                   vectors/ (FAISS + chunks + metadata)
                                            ↓
               ┌────────────────────────────┐
               │       rag.py CLI           │
               │  ask | search | ingest |   │
               │  reindex                   │
               └──────┬─────────────────────┘
                      │
             ┌────────┴──────────┐
             ▼                   ▼
     scripts/search.py    scripts/generate.py
      (FAISS + NIM)        (retrieval + LLM)
```

### RAG Commands (CLI)

| Comandă | Descriere |
|---------|-----------|
| `python rag.py ask "întrebare"` | RAG complet — caută + generează răspuns cu citări |
| `python rag.py search "cuvinte"` | Caută fragmente relevante în cursuri |
| `python rag.py ingest` | Parsează PDF-urile din `inbox/` în `processed/` |
| `python rag.py reindex` | Re-indexează embeddings (după adăugare PDF-uri noi) |

### Configurare

Cheia NVIDIA NIM în `.env`:
```
nvidia_api_key=nvapi-...
```

### Stack

- **Parsare PDF**: `pdfplumber` (text + metadate + poziționare cuvinte)
- **Chunking**: 500 cuvinte, 100 overlap
- **Embeddings**: `nvidia/nv-embed-v1` (4096d) via NVIDIA NIM
- **Vector DB**: FAISS (IndexFlatIP, cosine similarity)
- **LLM**: `meta/llama-3.3-70b-instruct` via NVIDIA NIM
- **Total**: 371 fragmente din 44 PDF-uri (4 materii)

## Semantic Search (QMD)

Indexul semantic `qmd` permite căutare locală 100% offline (BM25 + vector + rerank).

- **Colecție activă:** `concepts` → `concepts/**/*.md`
- **Index fizic:** `.qmd/index.sqlite`
- **După ingest:** rulează `/arscontexta:qmd:refresh` sau `qmd update && qmd embed`
- **MCP activ:** `.mcp.json` → 6 tool-uri auto-aprobate (search, vsearch, deep_search, get, multi_get, status)

## Jira Integration

Skill-ul `jira` permite interacțiunea cu Jira API direct din CLI.

| Comandă | Descriere |
|---------|-----------|
| `/arscontexta:jira:setup` | Configurează conexiunea Jira (base URL, email, API token) |
| `/arscontexta:jira:list` | Listează issue-uri dintr-un proiect |
| `/arscontexta:jira:create` | Creează issue nou în Jira |
| `/arscontexta:jira:link [ISSUE-123]` | Leagă notița curentă de issue Jira |
| `/arscontexta:jira:get [ISSUE-123]` | Vezi detalii issue |
| `/arscontexta:jira:search [JQL]` | Caută issue-uri după JQL |
| `/arscontexta:jira:sync` | Compară issue-uri Jira cu task-urile din `ops/queue/` |

Credentialele se salvează în `.jira/config.json` (ignorat de git).

## Condition-Based Maintenance

| Condiție | Prag | Acțiune |
|----------|------|---------|
| Concepte orfane >7 zile | Any | Rulează /conectează |
| Inbox items | >= 3 | Rulează /extrage |
| Observații nerezolvate | >= 5 | Rulează /rethink |

## Pipeline Compliance

PDF-urile intră în `inbox/`, trec prin `/extrage` → concepte în `concepts/`, apoi se arhivează în `archive/`.

## Metodologie

Vezi `.opencode/arscontexta/methodology/` (249 research claims) și `.opencode/arscontexta/reference/`.
