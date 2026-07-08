---
title: "AIASSIST — Agent OS local (ARS Contexta + Obsidian), Product Brief actualizat 30.06"
echipa: "B2 — Dorcea Eduard (lead) + Gheorghe Alin + 1 (de confirmat)"
repo: "DorceaEduard/ProiectEdi"
status: "Reorientat 30.06: din SaaS RAG web → agent OS second brain LOCAL. Scope tăiat pentru 10.07."
created: 2026-06-26
updated: 2026-06-30
---

# AIASSIST — Brief actualizat

> ⚠️ **CALENDAR NOU (decis 30.06 cu Mihaela):** practica se închide pentru TOATE grupele pe **10 iulie**. Mai aveți **3 ședințe**, dar DOAR **2 de build**:
> - **azi 30.06** (build) · **vin 03.07** 15-17 (build) — cele 2 ședințe de cod
> - **mar 07.07** = CV + aliniere prezentare finală (NU cod nou)
> - **vin 10.07** = prezentare + demo
>
> Tot MVP-ul de mai jos trebuie LIVE local până la finalul lui **03.07**.

> 🔄 **REORIENTARE (30.06):** brief-ul vostru inițial descria un **SaaS RAG web** complet (auth multi-user, vault shared, transcriere video/audio Whisper, deploy 4 platforme). Imposibil în 2 ședințe și reinventează lucruri care există deja. **Direcția confirmată de tutore:** un **second brain LOCAL** pe **ARS Contexta + Obsidian**. Nu construiți motorul RAG de la zero — stați pe ARS Contexta (are deja pipeline-ul + căutarea semantică locală `qmd`) și ingerați materialele cursului.

> 🎯 **MVP vs VISION — citește asta înainte de orice:** ținta celor 2 ședințe = **„upload PDF curs → întrebare → răspuns ancorat cu citare sursă", local.** Atât. În call s-a vorbit și despre un **„agent OS"** mai mare (interfață locală cu butoane, text-to-speech ElevenLabs, subagenți pe zone). **Acela = VISION / v2, NU MVP.** Cu 2 ședințe de build, dacă plecați după interfața OS rămâneți fără query-ul ancorat funcțional pe 10.07. Întâi bazele (motorul + ingest + citare), OS-ul îl construiți VOI după practică. Tutorele vă dă bazele; restul e al vostru.

## 1. Problema (neschimbat)
Un student de Automatică primește sute de pagini PDF, prezentări, notițe disparate. Volumul e copleșitor; răspunsurile de pe ChatGPT/YouTube nu sunt ancorate în ce a predat efectiv profesorul.

## 2. Soluția — second brain local, ancorat în curs
Un **vault second brain** (Obsidian) în care materialele de curs sunt procesate în note interogabile, plus un **agent** care răspunde la întrebări în limbaj natural **doar din materialele încărcate**, cu **citarea sursei exacte**. Anti-halucinație: dacă răspunsul nu e în surse, agentul spune „nu am asta în surse" — nu inventează.

## 3. Ce înseamnă „agent OS" (și ce NU construiți de la zero)

**Motorul = ARS Contexta** (vi-l setează tutorele):
- **pipeline** (`/process`, `/link`, area maps) — transformă materialul brut în note structurate, conectate
- **`qmd`** — index semantic **local, 100% offline** (BM25 + vector + rerank, embeddings cu model local GGUF). **Ăsta E RAG-ul vostru.** Nu mai aveți nevoie de pgvector/Supabase/cloud pentru căutare.
- **Obsidian** = vault-ul + interfața de navigare

**Ce construiți VOI deasupra** (asta e proiectul, nu „am instalat ARS Contexta"):
1. Un **pipeline de ingest** pe un curs REAL (PDF → markdown → procesat în note)
2. Un **agent de Q&A** (opencode + NVIDIA NIM) care interoghează `qmd` și răspunde **cu citare sursă**
3. Un **harness de evaluare** care dovedește că agentul e ancorat (răspunde corect din surse + spune „nu știu" pe out-of-scope)

Local-first: totul rulează pe mașina voastră. **Niciun deploy web, niciun auth, niciun vault shared în MVP** (alea = v2).

## 4. MVP redus — ce livrați până pe 10.07

| Prioritate | Component | Țintă |
|---|---|---|
| **MUST (azi)** | Setup ARS Contexta + Obsidian, vault funcțional, structură pe domeniul cursului; repo curat | trebuie |
| **MUST (azi → 03.07)** | Ingest: un curs real (PDF-uri) → markdown → procesat în note `qmd`-interogabile | trebuie |
| **MUST (03.07)** | Agent Q&A (opencode + NVIDIA NIM) care caută în `qmd` și răspunde **cu citare sursă** | trebuie |
| **MUST (03.07)** | Eval: 3-5 întrebări „gold" + min. 2 adversariale (răspuns corect = „nu am în surse") | trebuie |
| **VISION / v2** | „Agent OS": interfață locală cu butoane, text-to-speech (ElevenLabs), subagenți pe zone | NU în MVP |
| **VISION / v2** | Transcriere video/audio curs (Whisper local), flashcards, recuperare agentică | NU în MVP |
| **CUT** | SaaS web, auth multi-user, vault shared comunitate + moderare, admin, deploy cloud, mobile | scos |

## 5. Tooling
ARS Contexta (pipeline + `qmd` local) · Obsidian · opencode (agent în terminal) + NVIDIA NIM (LLM-ul agentului) · Whisper local DOAR la stretch. **Fără Supabase/pgvector/Render în MVP** — `qmd` acoperă RAG-ul local.

## 6. Epice de pornire (gata de spart în tichete Jira)

> **Echipa 2 e în urmă cu o ședință** (echipa 1 are deja repo cu plan; voi aveți doc-uri BMAD dar 0 ingest real). **Alin + al 3-lea membru: AZI intrați pe câte un task cu commit propriu.** Dorcea nu duce proiectul singur.

1. **EPIC: Vault & ARS Contexta** — setup ARS Contexta + Obsidian, structură (zone/scheme) pe domeniul cursului ales, `qmd` instalat și funcțional. Repo curat (vezi pasul de mai jos).
2. **EPIC: Ingest curs real** — alegeți UN curs, luați PDF-urile, treceți-le prin pipeline → note în vault → index `qmd`. *(criteriul (a): date reale)*
3. **EPIC: Agent Q&A cu citare** — agent opencode + NVIDIA NIM care: primește întrebare → caută în `qmd` → răspunde sintetizat **cu link la sursa exactă**. *(criteriul (b): componentă în servire)*
4. **EPIC: Eval & groundedness** — set de 3-5 întrebări gold + 2 adversariale; agentul trebuie să spună „nu am asta în surse" pe out-of-scope. *(criteriile (c)+(d): anti-halucinație — ăsta e diferențiatorul real față de ChatGPT)*
5. **STRETCH: extensii** — Whisper video, flashcards, recuperare agentică.

**Ordinea de atac:** 1 → 2 → 3 → 4. Astea = MVP-ul demonstrabil local.

## 7. Failure modes de tratat (criteriul (d), pentru notă)
- **Răspuns negăsit în surse** → agentul TREBUIE să zică „nu am în surse", nu să halucineze. Ăsta e testul-cheie.
- **PDF prost OCR-uit / scanat** → text murdar intră în index → răspunsuri proaste. De tratat la ingest.
- **NVIDIA NIM rate-limit (40 req/min/cont)** → agentul pică la query. Mitigare: cont propriu per membru.
- **Index `qmd` nereîmprospătat** după ingest nou → întrebări pe material care „nu există". `qmd refresh` în flow.

## 8. Definition of Done pentru demo (10.07)
- [ ] Vault local funcțional cu un curs real ingerat (PDF → note → index)
- [ ] Agent Q&A: pui o întrebare → primești răspuns sintetizat **cu citare sursă** — demonstrat live local
- [ ] Eval rulat: agentul răspunde corect la întrebările gold ȘI spune „nu știu" pe cele adversariale
- [ ] Repo curat: README cu setup + cum rulezi + failure modes; `_bmad/`, `.agents/`, `.opencode/` în `.gitignore`; commit-uri de la TOȚI 3
- [ ] CV pe GitHub Pages (07.07)

## Pasul imediat AZI (30.06)
1. **Curățați repo-ul:** adăugați `_bmad/`, `.agents/`, `.opencode/`, `_bmad-output/` (output-ul, nu doc-urile pe care le vreți păstrate) în `.gitignore`. Acum tot BMAD-ul e urcat în git = poluare (regula: ce ține de tooling-ul tău local NU se urcă în repo).
2. **Tutorele vă setează ARS Contexta + Obsidian** în ședință (EPIC 1).
3. **Alegeți cursul** pe care faceți ingest (EPIC 2) și spargeți EPIC 1+2 în tichete Jira.
4. Fiecare membru pe branch propriu → primul push cu muncă reală (note ingerate / config), nu doar doc-uri.
