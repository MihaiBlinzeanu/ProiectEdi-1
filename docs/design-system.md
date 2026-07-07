# RAGAssist - Design System

> Fața vizuală peste motorul vostru (`qmd` + agent). Scopul: un front în care pui o întrebare, iar răspunsul vine **ancorat în notele voastre, cu sursa la vedere**. Ăsta e diferențiatorul față de ChatGPT - designul îl scoate în față.
>
> Preview complet, funcțional: `docs/ui-preview.html` (deschide-l în browser). E stack-agnostic - îl porți pe Next.js, Vite sau îl lași HTML pentru demo.

## 1. Direcția - "Reading Room"

Nu jucăuș, ci **calm, studios, de încredere**. Un birou de studiu, nu o aplicație de productivitate. Textul e rege (citești răspunsuri lungi), sursele sunt comoara. Paletă caldă de hârtie + cerneală, un singur accent rece (pine) pentru brand și unul cald (ochre) pentru surse.

Principii:
- **Sursa e cetățean de rang 1.** Fiecare afirmație are un marcaj `[n]`; sub răspuns, carduri de sursă cu titlul notei + cursul + locația.
- **Ancorare vizibilă.** Când răspunsul nu e în corpus, o stare distinctă „nu în surse" - nu inventezi.
- **Lizibilitate lungă.** Serif pentru răspunsuri (confort la citit), sans pentru UI, mono pentru referințe tehnice.

## 2. Culori (tokens oklch)

### Light (implicit - "paper")
```css
--paper:        oklch(0.977 0.006 95);   /* fundal, hârtie caldă */
--paper-2:      oklch(0.955 0.008 90);   /* sidebar, zone secundare */
--card:         oklch(0.994 0.003 95);   /* carduri, suprafețe ridicate */
--ink:          oklch(0.27 0.018 250);   /* text principal, slate profund */
--ink-soft:     oklch(0.44 0.02 250);    /* text secundar */
--ink-faint:    oklch(0.60 0.015 250);   /* labels, meta */
--pine:         oklch(0.46 0.072 185);   /* brand, primary, focus */
--ochre:        oklch(0.66 0.105 72);    /* SURSE - accentul cald, iese în față */
--ochre-text:   oklch(0.50 0.10 66);     /* text pe fundal ochre-soft */
--border:       oklch(0.90 0.01 250);
--danger:       oklch(0.55 0.15 28);     /* starea „nu în surse" */
```

### Dark ("night reading" - opțional)
```css
--paper:        oklch(0.20 0.015 250);
--paper-2:      oklch(0.24 0.016 250);
--card:         oklch(0.25 0.016 250);
--ink:          oklch(0.93 0.008 95);
--ink-soft:     oklch(0.75 0.012 250);
--ink-faint:    oklch(0.58 0.015 250);
--pine:         oklch(0.68 0.09 185);    /* mai luminos pe fundal închis */
--ochre:        oklch(0.74 0.11 72);
--danger:       oklch(0.62 0.15 28);
```

Regulă: neutrele au un strop de hue (250 = slate rece), nu gri pur. Ochre e SINGURA culoare caldă - de aceea sursele atrag ochiul.

## 3. Tipografie

| Rol | Font | Unde |
|-----|------|------|
| Display + răspunsuri | **Newsreader** (serif editorial) | întrebări, textul răspunsului, titluri surse |
| UI | **IBM Plex Sans** | butoane, labels, input, navigație |
| Mono | **IBM Plex Mono** | referințe (`concepts/`, `qmd`), badge-uri tehnice |

Import: `https://fonts.googleapis.com/css2?family=Newsreader:...&family=IBM+Plex+Sans:...&family=IBM+Plex+Mono:...`

Scală: întrebare 25px/500, răspuns 18.5px/1.62 (serif, lizibil), UI 14-15px, meta 11px.

## 4. Componente cheie

**Source card** (vedeta) - `border-left: 3px solid var(--ochre)`, badge numeric, titlul notei în serif, meta mono cu cursul (pine) + calea. Hover: ridicare 2px + umbră. Astea leagă răspunsul de `qmd`.

**Inline citation** `[n]` - superscript, `ochre-text` pe `ochre-soft`, clickabil → scroll la cardul sursei.

**Answer** - serif, paragrafe scurte, `<strong>` pentru termenii-cheie. Nu wall-of-text.

**Refusal / „nu în surse"** - box cu `danger` soft, badge „NU ÎN SURSE", explică ce ACOPERĂ corpusul și de ce nu inventează. Ăsta e testul vostru de groundedness, arătat vizual.

**Composer** - input + buton pine, focus ring pine. Hint dedesubt: „fără sursă → nu în surse, nu halucinație".

**Sidebar corpus** - materiile ingerate cu numărul de note (din `qmd`). Arată domeniul acoperit.

**Topbar** - contextul curent + un pill `qmd · BM25 + vector · offline` (spune că-i local, nu cloud).

Radius 12-14px, umbre discrete, textură subtilă de puncte pe fundal (aer de hârtie).

## 5. Cum se leagă de motor

```
input → qmd search (BM25 + vector, local) → top-k note
      → agent (opencode + NVIDIA NIM) sintetizează DOAR din notele returnate
      → UI: răspuns + inline [n] + source cards (din metadata notelor)
      → dacă qmd nu întoarce nimic relevant → starea „nu în surse"
```

Sursele din carduri = exact fișierele pe care `qmd` le-a întors (titlu = numele notei, meta = folder + curs). Nimic inventat: dacă nu vine din qmd, nu apare card.

## 6. De pornit

1. Deschide `docs/ui-preview.html` - ăsta e target-ul vizual. La colocviu poate fi chiar „frontul" (static, cu un exemplu real).
2. Pentru varianta conectată: un Next.js/Vite minimal, pui tokenii de mai sus în CSS, refaci componentele din preview, iar în locul datelor statice apelezi `qmd` + agentul vostru.
3. Ține datele reale: concepte din materiile voastre (Automatizarea Clădirilor, Rețelistică, Web). Demo-ul e mai puternic pe cursul vostru real decât pe exemple inventate.
