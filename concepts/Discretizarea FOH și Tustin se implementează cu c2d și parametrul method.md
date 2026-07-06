---
description: "Matlab c2d(sys, Ts, 'foh'|'zoh'|'tustin') discretizează sisteme continue. Ts=-1 pentru perioadă nespecificată."
materii: ["[[Sisteme Automate]]"]
type: algorithm
source: "SA Laborator 8_2026.pdf"
confidence: established
---

Funcția c2d(sys, Ts, method) discretizează sisteme LIT continue. Metode: 'zoh' — răspuns echivalent la intrare treaptă, 'foh' — extrapolare de ordinul întâi, 'tustin' — transformare biliniară. sys = tf(num, den, Ts) creează un sistem discret; Ts = 0 înseamnă continuu, Ts = -1 sau [] înseamnă perioadă nespecificată. Pe măsură ce perioada de eșantionare scade, răspunsul la treaptă se apropie de cel continuu.

**Topics:** [[Sisteme Automate]]
