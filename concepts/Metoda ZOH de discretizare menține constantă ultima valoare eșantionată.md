---
description: "ZOH menține semnalul constant între eșantioane și introduce o întârziere de tact; nu se recomandă pentru aproximarea regulatoarelor."
materii: ["[[Sisteme Automate]]"]
type: definition
source: "SA Laborator 6_2026.pdf"
confidence: established
---

Discretizarea ZOH presupune că semnalul de intrare este constant între două eșantioane: u(t) = u[k] pentru kT ≤ t < (k+1)T. Transformarea utilizează modelul G(z) = (1 - z⁻¹)·Z{G(s)/s}. Metoda este inerentă proceselor continue comandate de regulator numeric și introduce un tact de întârziere. Nu se recomandă pentru aproximarea unui regulator sau filtru — pentru aceasta se preferă metoda Tustin.

**Topics:** [[Sisteme Automate]]
