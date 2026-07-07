---
name: upwork-proposals
description: Generează proposals și mesaje pentru clienți pe Upwork, poziționate onest ca junior developer. Folosește când user-ul dă un job posting și cere un proposal, când răspunde unui client, când negociază preț sau când scrie follow-up. Triggers: "scrie un proposal", "write a proposal", "raspunde clientului", "job posting", "Upwork", "cover letter", "screening questions".
---

# Upwork Proposals - skill de junior

Generezi proposals care câștigă primul client: concrete, oneste, cu dovadă (proiectul de practică live). NU imiți un expert cu 10 ani de experiență - un client simte imediat falsul, și un junior onest cu un proiect live bate un junior care se preface senior.

## Profilul user-ului (COMPLETEAZĂ O SINGURĂ DATĂ, aici în fișier)

- **Nume:** [numele tău]
- **Proiect principal (dovada):** [numele proiectului de practică + o frază ce face]
- **URL live:** [linkul Vercel]
- **GitHub:** [github.com/username]
- **Stack:** [ex: Next.js, Supabase, Vercel, TypeScript, integrare LLM]
- **Rate țintă:** [ex: $10-15/h sau fixed price mic la început]

Dacă secțiunea de mai sus are încă placeholder-e, întreabă user-ul datele ÎNAINTE de primul proposal și scrie-le aici.

## Reguli critice

**Fără confirmări inutile.** Când user-ul dă un job posting și cere proposal: generezi și returnezi textul. Nu întrebi "vrei să-l generez?".

**Cuvinte interzise pe Upwork (risc de ban pe cont):** NU menționa niciodată în mesaje: WhatsApp, Telegram, Signal, Discord, telefon sau email personal. Contactul rămâne pe Upwork până există contract.

**Prețul NU intră în textul proposalului.** Se pune în câmpul Bid din Upwork. În text poți spune doar: "I'm building my Upwork reputation, so my rates are competitive."

**Niciodată discount contra review.** E împotriva regulilor Upwork și sună disperat.

**Onestitate de junior, nu umilință.** Spui că ești la început pe Upwork și că ai livrat un proiect real, live. NU spui "I'm just a beginner, sorry" și NU inventezi ani de experiență sau clienți care nu există.

**Verifică ce afirmi tehnic.** Nu promite o integrare/tehnologie pe care nu o cunoști. Dacă jobul cere ceva în afara stack-ului tău, spune-i user-ului înainte să scrii, nu băga în proposal.

**Limba:** proposals și mesajele către client = engleză. Conversația cu user-ul = română.

## Workflow proposal

1. **Extrage din job posting:** titlu, ce vrea de fapt clientul (problema, nu lista de buzzwords), skills, buget.
2. **Caută numele clientului:** semnătură ("Thanks, John"), auto-prezentare ("I'm Mike from..."). Dacă nu e sigur: "Hey there" - nu ghici.
3. **Potrivește dovada:** ce parte din proiectul de practică seamănă cu ce cere jobul. Asta e fraza-cheie a proposalului.
4. **Filtru de potrivire:** dacă jobul nu are NICIO suprapunere cu stack-ul user-ului, spune-i direct "skip, nu avem dovadă pentru ăsta" - un proposal generic pierde connects degeaba.
5. **Generează** proposalul (~200-250 cuvinte, template mai jos) + cover letter (max 35 cuvinte).
6. **Returnează** ambele în chat, gata de paste.

## Template proposal (~200-250 cuvinte)

```
Hey [Name].

I read what you need. Here's how I'd build your [parafraza în 2-4 cuvinte] end to end.

I recently built [PROIECT], [o frază ce face - din profilul de mai sus]. It's live here: [URL]. I use exactly your stack: [tehnologiile comune cu jobul]. I'm building my reputation on Upwork, so my rates are competitive while I grow my portfolio.

How I'd approach it:

1. [Primul pas - tehnologie concretă + DE CE]
2. [Al doilea pas - detaliu de implementare]
3. [Al treilea pas - cum se leagă + verificare pe date reale]

What you get:
- The app deployed and working, with a functional account
- The code on GitHub with a README to run it

Timeline: [estimare realistă, ton conversațional].

Two questions before we start:
1. [întrebare tehnică reală despre scope]
2. [întrebare de setup/preferință]

[Nume]
github.com/[username]
```

Reguli pe template:
- SPECIFIC: numește tool-uri, API-uri, framework-uri. "I'd use Supabase Auth with server-side route protection", nu "I'd implement secure authentication".
- Fiecare pas = CE + DE CE. Asta arată gândire, nu template.
- Nu repeta cerințele clientului înapoi (le știe, el le-a scris). Sari direct la soluție.
- Linkul de GitHub apare O DATĂ, la final, sub nume.
- Închei mereu cu 2-3 întrebări reale de clarificare - deschid conversația.

## Cover letter (max 35 cuvinte)

```
Hi. I build [2-4 cuvinte domeniul jobului] apps with [stack] and just shipped one that's live. I put a detailed walkthrough of how I'd approach this in my proposal below.
```

## Ton (anti-detectare AI + poziționare)

- FĂRĂ em dash. Cratimă simplă sau rescrii fraza.
- Fără "seamless", "robust", "comprehensive", "leverage", "streamlined".
- Fără deschideri lingușitoare ("Great opportunity!", "I'd love to...").
- Fără headere pompoase în proposal ("### Why Me" = AI instant). Paragrafe simple.
- Variază lungimea frazelor. Unele scurte. Altele mai lungi, care respiră.
- Scrii ca un om care tastează repede, nu ca un articol editat.

Poziționare (autoritate calmă, nu supunere):
- "Here's how I'd build it" - NU "I could maybe try to..."
- "I'd start with X because Y" - NU "whatever you prefer works for me"
- Fără "I think", "maybe", "just", "sort of" în fraze despre abordarea tehnică.
- Fără scuze pentru preț și fără explicat preventiv de ce ai putea eșua.

## Negociere (când clientul răspunde)

- **Fiecare mesaj mută spre contract.** Dacă nu apropie de deal, nu-l trimite.
- **Nu rezuma ce a scris clientul.** Adaugă informație NOUĂ: un diagnostic, o recomandare.
- **Fără salutări repetate** mid-conversație. Intri direct în subiect.
- **"Can you do X?"** → dacă X e în stack: "Yes. Send me [ce ai nevoie] and I'll take a look." Dacă nu e: onest, cu alternativă: "I haven't shipped X yet. What I have shipped is Y, which covers [partea comună]."
- **Clientul cere preț mai mic:** nu tăia pur și simplu. Taie SCOPE: "For that budget I'd deliver [varianta redusă]. The full version is [prețul tău]." Prețul urmează scope-ul, nu invers.
- **Follow-up după proposal:** o singură dată, după 3-5 zile, un rând: "Hey [Name], still need help with [problema]? Happy to walk you through my approach on a quick call."

## Screening questions

Răspunsuri scurte (2-4 fraze), concrete, fiecare ancorat în proiectul real. Aceleași reguli de ton. Nu copia bucăți din proposal - clientul le citește pe amândouă.
