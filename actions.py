import os
import requests
from dotenv import load_dotenv

# Lädt die Variablen aus der .env Datei
load_dotenv()

HA_URL = os.getenv("HA_URL", "http://localhost:8123")
HA_TOKEN = os.getenv("HA_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json"
}

def call_ha(domain, service, entity_id):
    try:
        url = f"{HA_URL}/api/services/{domain}/{service}"
        requests.post(
            url,
            headers=HEADERS,
            json={"entity_id": entity_id},
            timeout=5
        )
        log("ACTION", f"{service} {entity_id}")
    except Exception as e:
        log("ERROR", str(e))

def turn_on(entity):
    domain = entity.split(".")[0]
    call_ha(domain, "turn_on", entity)

def turn_off(entity):
    domain = entity.split(".")[0]
    call_ha(domain, "turn_off", entity)

def get_weather():
    """Holt den aktuellen Wetterstatus aus Home Assistant"""
    try:
        url = f"{HA_URL}/api/states/weather.forecast_home"
        response = requests.get(url, headers=HEADERS, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            state = data.get("state") # z.B. "sunny", "cloudy"
            temp = data.get("attributes", {}).get("temperature") # Temperatur
            
            # Einfache Übersetzung für die Sprachausgabe
            uebersetzung = {
                "sunny": "sonnig",
                "cloudy": "bewölkt",
                "partlycloudy": "leicht bewölkt",
                "rainy": "regnerisch",
                "snowy": "verschneit",
                "windy": "windig",
                "clear-night": "klar"
            }
            
            wetter_deutsch = uelement = uebersetzung.get(state, state)
            
            return f"Das Wetter ist aktuell {wetter_deutsch} bei {temp} Grad."
        else:
            return "Ich konnte keine Wetterdaten abrufen."
    except Exception as e:
        log("ERROR", f"Wetter-Abfrage fehlgeschlagen: {str(e)}")
        return "Das Wetter ist aktuell nicht verfügbar."
