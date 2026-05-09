# TextLens — AI Analyzátor Textu

Webová aplikácia na analýzu textu poháňaná Groq API a modelom LLaMA 3.3 70B. Funguje ako jednoduchý HTML súbor — bez servera, bez inštalácie.

## Funkcie

- **5 režimov analýzy** — Zhrnutie, Kľúčové slová, Sentiment, Vysvetli jednoducho, Školské poznámky
- **Nahrávanie súborov** — podpora TXT, MD, PDF a DOCX (max 3 súbory)
- **Drag & drop** — súbory môžeš priamo pretiahnuť do aplikácie
- **Výsledky v slovenčine** — všetky výstupy sú v slovenskom jazyku
- **Štatistiky textu** — počet slov, viet a odhadovaný čas čítania

## Použitie

1. Otvor `TextLens.html` v prehliadači
2. Zadaj svoj [Groq API kľúč](https://console.groq.com) a klikni **Uložiť kľúč**
3. Nahraj súbory alebo vlož text priamo
4. Vyber režim analýzy v ľavom paneli
5. Klikni **Analyzovať**

## Požiadavky

- Moderný prehliadač (Chrome, Firefox, Edge)
- Groq API kľúč — zadarmo na [console.groq.com](https://console.groq.com)

## Technológie

- HTML / CSS / JavaScript
- [Groq API](https://groq.com) — LLaMA 3.3 70B
- [PDF.js](https://mozilla.github.io/pdf.js/) — čítanie PDF súborov
- [Mammoth.js](https://github.com/mwilliamson/mammoth.js) — čítanie DOCX súborov
