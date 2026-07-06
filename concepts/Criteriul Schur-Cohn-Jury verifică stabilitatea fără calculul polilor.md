---
description: "Criteriul Jury verifică dacă rădăcinile polinomului caracteristic P(z) se află în interiorul cercului unitate prin condiții și un tabel."
materii: ["[[Sisteme Automate]]"]
type: algorithm
source: "SA Laborator 7_2026.pdf"
confidence: established
---

Criteriul Schur-Cohn-Jury verifică stabilitatea unui sistem numeric pe baza polinomului caracteristic P_c(z) = a₀zⁿ + a₁zⁿ⁻¹ + ... + aₙ. Condiții obligatorii: (1) |aₙ| < a₀, (2) P_c(1) > 0, (3) (-1)ⁿ·P_c(-1) > 0. Se completează tabelul lui Jury — prima linie cu coeficienții în ordine crescătoare, a doua inversată, apoi se calculează recursiv. Sistemul este stabil dacă toate elementele noi calculate respectă condiția. Pentru sisteme de ordinul I se folosesc doar primele două condiții.

**Topics:** [[Sisteme Automate]]
