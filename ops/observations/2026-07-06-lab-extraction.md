---
type: observation
session: 2026-07-06
related: "[[Sisteme Automate]] [[Retelistică]]"
---

Extracted 19 new concepts from lab PDFs: 17 for Sisteme Automate (11 laboratoare) + 2 for Retelistică (Lab4 — singurul cu text citibil). 

**Friction:** Majoritatea PDF-urilor de laborator Retelistică (Lab1, 2, 3, 6, 8) sunt scanuri fără text layer — nu se poate extrage conținut cu pdf-text-reader. Ar necesita OCR.

**Friction:** Materii values în Supabase nu au `[[...]]` brackets deși concepts.sql le includea. La INSERT nou, trebuie să stochez fără brackets ca să meargă `.contains()` în site.

**Done:**
- Butoane Login/Test mărite
- Buton "Formule și exerciții" în sidebar (filtrează type=formula|algorithm|example)
- Plan de învățare grupat pe surse/PDF în loc de type
- 19 concepte noi din laboratoare în concepts/ și Supabase
- Sidebar counts actualizate (SA: 24, Retelistică: 26)
