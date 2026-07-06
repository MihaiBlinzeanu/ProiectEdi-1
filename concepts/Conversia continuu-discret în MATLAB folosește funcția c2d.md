---
description: "Funcția c2d(sys, T, method) convertește un sistem continuu în discret cu extrapolator de ordin zero și perioadă T."
materii: ["[[Sisteme Automate]]"]
type: algorithm
source: "SA Laborator 4_2026.pdf"
confidence: established
---

Matlab permite conversia continuu-discret cu instrucțiunea sysd = c2d(sys, T) care realizează conversia cu extrapolator de ordin zero. Conversia inversă se face cu sysc = d2c(sysd). Sistemele discrete se introduc cu tf(num, den, Ts), zpk(z, p, k, Ts) sau ss(a, b, c, d, Ts). Răspunsul indicial se trasează cu dstep(num, den, n), iar răspunsul la semnal arbitrar cu dlsim(num, den, u).

**Topics:** [[Sisteme Automate]]
