# Lokaler KI-Assistent auf Raspberry Pi 4 Basis

Das Ziel: Ein smarter Assistent für mein Zimmer, der Geräte (wie meinen Ventilator oder das Licht) steuert. Da mir herkömmliche Lösungen wie Alexa oft zu unflexibel und limitiert sind, baue ich hier ein eigenes, intelligenteres System auf.

Das wichtigste Prinzip dabei: **Absolut keine Cloud!** Alle Berechnungen und Daten bleiben zu 100 % lokal auf meinem Raspberry Pi 4B, um die Privatsphäre zu sichern.

---

## Features (Aktueller Stand)

Auch wenn die Spracheingabe noch in Arbeit ist, steht das gesamte "Gehirn" des Assistenten bereits und wird über ein Terminal-Interface bedient:

* **Intelligentes Request-Routing:** Das System analysiert eingehende Texte und entscheidet dynamisch über den nächsten Schritt:
    * **Simple:** Einfacher Smalltalk wird direkt abgefangen (schont die Hardware).
    * **Device:** Erkennt Steuerungsbefehle (z. B. "Licht an") und triggert die Smart-Home-Aktion.
    * **Knowledge:** Bei komplexen Wissensfragen wird automatisch eine Websuche initiiert.
* **Home Assistant Integration:** Direkte Anbindung an die Home Assistant API, um reale Hardware (z. B. smarte Steckdosen) im Zimmer zu schalten.
* **Websuche & Kontext-Anreicherung:** Bei aktuellen Fragen startet das System eine asynchrone Websuche (via DuckDuckGo API) und füttert das lokale Sprachmodell mit den Suchergebnissen, um korrekte Antworten zu garantieren.

---

##  Technische Herausforderungen (Hardware-Limits)

Da ich mich strikt gegen Cloud-APIs (wie OpenAI) entschieden habe, muss der Pi 4B das Sprachmodell selbst berechnen. Das war die größte Hürde:

* **Modell-Optimierung:** Größere Modelle (wie `qwen2.5:3b`) liefen extrem langsam und führten zu Timeouts.
* **Die Lösung:** Der Wechsel auf `llama3.2:1b` über Ollama war der Durchbruch. Das Modell ist extrem kompakt, antwortet auf dem Pi 4B verhältnismäßig flüssig und liefert fehlerfreie, präzise Ergebnisse.

---

## Code-Architektur (Modularer Aufbau)

Um Spaghetti-Code zu vermeiden, ist das Projekt in logische Module unterteilt:

* `main.py` — Der Einstiegspunkt mit der zentralen Eingabe-Schleife.
* `router.py` — Übernimmt das Parsing und Routing der Usereingaben.
* `knowledge.py` — Holt bei Bedarf via DuckDuckGo aktuelle Zusatzinformationen aus dem Web.
* `llm.py` — Steuert die API-Abfragen an das lokale Ollama-Modell.
* `actions.py` — Verarbeitet die REST-API-Calls in Richtung Home Assistant.
* `state.py` & `logger.py` — Verwalten den Systemzustand und protokollieren Events in `assistant.log`.

---

##  Ausblick & Roadmap (Was noch geplant ist)

Das System ist als erweiterbares MVP (Minimum Viable Product) gedacht. Als Nächstes ist geplant:

1. **Voice-Erkennung (Speech-to-Text):** Integration einer lokalen Spracheingabe, damit das System nicht mehr über die Tastatur gefüttert werden muss.
2. **Sprach-Antwort (Text-to-Speech):** Einbindung einer schnellen, lokalen TTS-Engine (geplant ist **Piper**), damit der Assistent auch akustisch antworten kann.
3. **Schnellere Antwortzeiten:** Optimierung des Codes (ggf. Wechsel auf einen Raspberry Pi 5 oder einen Mini-PC), um die Latenz bei der KI-Generierung weiter zu drücken.
4. **Hardware-Gehäuse:** Entwurf einer eigenen, optisch ansprechenden Tisch-Station für den Pi, die ich mit dem 3D-Drucker ausdrucken werde.
