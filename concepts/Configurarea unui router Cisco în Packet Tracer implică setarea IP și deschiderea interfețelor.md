---
description: "Routerele Cisco se configurează inițial prin portul consolă, apoi se setează adresa IP și se activează interfața cu 'no shutdown'."
materii: ["[[Retelistică]]"]
type: algorithm
source: "Lab4.pdf"
confidence: supported
---

Configurarea inițială a unui router Cisco: (1) conexiune directă prin portul consolă (cablu consolă RJ45-DB9 sau USB); (2) trecerea în modul Privileged EXEC (enable); (3) configurarea interfeței (configure terminal → interface G0/0/0); (4) setarea adresei IP (ip address 192.168.10.1 255.255.255.192); (5) activarea interfeței (no shutdown); (6) verificarea cu show ip interface brief. Implicit, interfețele routerelor Cisco sunt oprite (administratively down).

**Topics:** [[Retelistică]]
