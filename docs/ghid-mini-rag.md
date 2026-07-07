# Mini-RAG pentru SecondBrain - ghid pas cu pas

Ce aveți acum: căutare prin cuvinte-cheie în concepte, cu citarea sursei. Răspunsul e o concatenare a descrierilor găsite (`generateAnswer` din `site/index.html`).

Ce adăugăm: un **model LLM care formulează răspunsul** pe baza pasajelor găsite de căutarea voastră. Asta e etapa de "generation" din RAG. Căutarea (retrieval) rămâne a voastră, pe cuvinte-cheie - și e OK să spuneți asta onest la prezentare: "RAG cu retrieval pe cuvinte-cheie".

Efort estimat: ~1 oră. Trei pași: o funcție serverless nouă, o modificare mică în frontend, o variabilă de mediu pe Vercel.

## De ce serverless și nu direct din browser

Cheia NVIDIA NU are voie să apară în `index.html` - orice vizitator ar vedea-o cu View Source și ar folosi-o pe contul vostru. Aceeași lecție ca cu tokenul comis în git: secretele stau pe server, nu în client. Vercel vă dă funcții serverless gratis: orice fișier din folderul `api/` de la rădăcina repo-ului devine un endpoint.

## Pasul 1: funcția serverless

Creați fișierul `api/answer.js` la RĂDĂCINA repo-ului (nu în `site/`):

```js
export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { question, passages } = req.body || {};
  if (!question || !Array.isArray(passages) || passages.length === 0) {
    return res.status(400).json({ error: 'question și passages sunt obligatorii' });
  }

  // contextul = pasajele găsite de căutarea voastră, numerotate ca să poată cita
  const context = passages
    .map((p, i) => `[${i + 1}] ${p.title}\n${p.description}`)
    .join('\n\n');

  const r = await fetch('https://integrate.api.nvidia.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.NVIDIA_API_KEY}`,
    },
    body: JSON.stringify({
      model: 'mistralai/mistral-large-3-675b-instruct-2512',
      temperature: 0.2,
      max_tokens: 500,
      messages: [
        {
          role: 'system',
          content:
            'Ești un asistent de studiu. Răspunzi DOAR pe baza contextului primit (notițe de curs). ' +
            'Dacă răspunsul nu se află în context, spui exact: "Nu am găsit informații relevante în notele de curs." ' +
            'Răspunzi în română, concis, și marchezi sursele folosite cu [1], [2] etc.',
        },
        {
          role: 'user',
          content: `Context:\n${context}\n\nÎntrebare: ${question}`,
        },
      ],
    }),
  });

  if (!r.ok) {
    return res.status(502).json({ error: 'Eroare LLM: ' + r.status });
  }

  const data = await r.json();
  return res.status(200).json({ answer: data.choices[0].message.content });
}
```

De ce `mistral-large`: text-only dar rapid (sub o secundă) și stabil pe NVIDIA NIM. Aici nu aveți nevoie de vision.

## Pasul 2: vercel.json - lasă /api să treacă

`vercel.json` are acum un rewrite care trimite TOT către `index.html` - ar înghiți și `/api/answer`. Schimbați sursa rewrite-ului ca să excludă `/api`:

```json
{
  "buildCommand": "",
  "outputDirectory": "site",
  "devCommand": "npx serve site",
  "installCommand": "",
  "framework": null,
  "rewrites": [
    {
      "source": "/((?!api/).*)",
      "destination": "/index.html"
    }
  ]
}
```

## Pasul 3: frontend - folosește LLM-ul, cu fallback

În `site/index.html`, înlocuiți în handler-ul lui `sendBtn` apelul la `generateAnswer` cu o variantă care încearcă întâi LLM-ul și cade înapoi pe concatenare dacă API-ul e down (demo-ul nu moare niciodată):

```js
async function generateAnswerLLM(question, results) {
  // refuz curat când căutarea nu găsește nimic - comportamentul existent rămâne
  if (!results || results.length === 0) {
    return generateAnswer(question, results);
  }
  try {
    const r = await fetch('/api/answer', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        question,
        passages: results.map(x => ({ title: x.title, description: x.description })),
      }),
    });
    if (!r.ok) throw new Error('API ' + r.status);
    const { answer } = await r.json();
    return {
      html: `<p>${escapeHtml(answer).replace(/\[(\d+)\]/g, '<span class="cite">$1</span>')}</p>`,
      sources: results.map(x => ({ id: x.id, title: x.title, materii: x.materii, source: x.source })),
      refusal: false,
    };
  } catch (_) {
    // fallback: comportamentul actual (concatenare cu citare)
    return generateAnswer(question, results);
  }
}
```

Și în handler:

```js
// înainte:
const { html, sources, refusal } = generateAnswer(q, results);
// după:
const { html, sources, refusal } = await generateAnswerLLM(q, results);
```

`generateAnswer` NU se șterge - rămâne fallback-ul.

## Pasul 4: cheia pe Vercel

1. Vercel dashboard → proiectul vostru → Settings → Environment Variables
2. Nume: `NVIDIA_API_KEY`, valoare: cheia NVIDIA (a unuia dintre voi), toate environment-urile
3. Redeploy (Deployments → ⋯ → Redeploy), altfel variabila nu e văzută

Local puteți testa cu `npx vercel dev` (citește variabila dintr-un `.env.local` la rădăcină - care e în `.gitignore`, nu se comite).

## Cum verificați că merge

1. Întrebare normală ("ce este un switch?") → răspuns formulat, nu descrieri lipite, cu [1] [2]
2. Întrebare cu sinonim/parafrază pe un concept existent → dacă căutarea găsește pasajul, LLM-ul formulează; dacă nu găsește → refuz (limitarea retrieval-ului lexical - o menționați onest la prezentare ca "next step: căutare semantică")
3. Întrebare complet în afara materiilor ("cine a câștigat mondialul?") → "Nu am găsit informații relevante" - demo-ul anti-halucinație
4. Opriți temporar variabila de mediu → aplicația cade elegant pe concatenarea veche, nu crapă

Punctele 1+3 sunt exact demo-ul pentru colocviu, și acoperă BRAIN-14/15 (setul de întrebări de test + eval).

## Ce spuneți la prezentare

"Asistent de studiu cu răspunsuri ancorate în notele de curs: căutarea găsește conceptele relevante pe cuvinte-cheie, un LLM formulează răspunsul strict din pasajele găsite și citează sursele, iar când informația nu există în note, refuză să inventeze. Next step planificat: retrieval semantic cu embeddings, ca sinonimele să fie găsite."

Fiecare frază de acolo e apărabilă la întrebări.
