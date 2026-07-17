# Lokaler KI-Assistent auf Raspberry Pi 4 Basis

Das Ziel: Ein smarter Assistent für mein Zimmer, der Geräte (wie meinen Ventilator oder das Licht) steuert. Da mir herkömmliche Lösungen wie Alexa oft zu unflexibel und limitiert sind, baue ich hier ein eigenes, intelligenteres System auf.

Das wichtigste Prinzip dabei: **Absolut keine Cloud für die Intelligenz!** Alle Berechnungen und Daten des Sprachmodells bleiben zu 100 % lokal auf meinem Raspberry Pi 4B, um die Privatsphäre zu sichern.

---

## Features (Aktueller Stand)

Das System verfügt mittlerweile über ein funktionierendes Sprach-Interface (Voice) und ein intelligentes "Gehirn":

*   **Intelligentes Request-Routing:** Das System entscheidet über den nächsten Schritt:
    *   *Simple:* Einfacher Smalltalk wird direkt abgefangen (schont die Hardware).
    *   *Device:* Erkennt Steuerungsbefehle (z. B. "Licht an") und triggert die Smart-Home Aktion.
    *   *Knowledge:* Bei komplexen Wissensfragen wird automatisch eine Websuche initiiert.
*   **Spracherkennung & Sprachausgabe (Voice):** Das System kann bereits über das Mikrofon (`SpeechRecognition`) gesteuert werden. Die Sprachausgabe ist in Arbeit; aktuell antwortet das System noch über ein Terminal-Interface oder eine einfache Text-to-Speech-Engine, die Integration einer modernen KI-Stimme (`edge-tts`) ist der nächste Schritt im Code.
*   **Home Assistant Integration:** Direkte Anbindung an die Home Assistant API, um reale Hardware (z. B. smarte Steckdosen) im Zimmer zu schalten.
*   **Websuche & Kontext-Anreicherung:** Bei aktuellen Fragen startet das System eine Websuche (via DuckDuckGo API) und füttert das lokale Sprachmodell mit den Suchergebnissen, um korrekte Antworten zu garantieren.

---

## Technische Herausforderungen (Hardware-Limits)

Da ich mich strikt gegen Cloud-APIs (wie OpenAI) entschieden habe, muss der Pi 4B das Sprachmodell selbst berechnen. Das war die größte Hürde:

*   **Modell-Optimierung:** Größere Modelle (wie qwen2.5:3b) liefen extrem langsam und führten zu Timeouts.
*   **Die Lösung:** Der Wechsel auf `llama3.2:1b` über Ollama war der Durchbruch. Das Modell ist extrem kompakt, antwortet auf dem Pi 4B verhältnismäßig flüssig und liefert fehlerfreie, präzise Ergebnisse.

---


## Ausblick & Roadmap (Was noch geplant ist)

Das System ist als erweiterbares MVP (Minimum Viable Product) gedacht. Als Nächstes ist geplant:

*   **Integration der KI-Stimme (`edge-tts`):** Umbau der Sprachausgabe in der `main.py`, damit der Assistent mit einer flüssigen, natürlichen Stimme statt abgehacktem Computer-Sound antwortet.
*   **Hardware-Gehäuse (CAD):** Entwurf einer eigenen, optisch ansprechenden Tisch-Station für den Pi, die Aussparungen für das Mikrofon und die Kühlung besitzt und mit dem 3D-Drucker ausgedruckt wird.
*   **Schnellere Antwortzeiten:** Optimierung des Codes (ggf. Wechsel auf einen Raspberry Pi 5 oder einen Mini-PC), um die Latenz bei der lokalen KI-Generierung weiter zu drücken.


---

## Installation & Sicherheit

Aus Sicherheitsgründen sind alle API-Token und URLs in einer lokalen Umgebungsvariable ausgelagert und werden nicht auf GitHub hochgeladen.

1. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
