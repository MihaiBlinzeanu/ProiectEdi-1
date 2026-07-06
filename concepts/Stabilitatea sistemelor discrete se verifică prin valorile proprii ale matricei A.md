---
description: "Pentru un sistem discret x[k+1] = A·x[k] + B·u[k], stabilitatea impune ca toate valorile proprii ale matricei A să aibă |λ| < 1."
materii: ["[[Sisteme Automate]]"]
type: algorithm
source: "SA Laborator 7_2026.pdf"
confidence: established
---

Un sistem discret definit prin reprezentarea în spațiul stărilor x[k+1] = A·x[k] + B·u[k] este stabil dacă toate valorile proprii ale matricei A au modulul subunitar. Valorile proprii se calculează din det(A - λI) = 0. Comportamentul sistemului în timp este determinat de Aᵏ — dacă valorile proprii sunt în cercul unitate, Aᵏ → 0 și sistemul converge.

**Topics:** [[Sisteme Automate]]
