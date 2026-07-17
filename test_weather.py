import requests

HA_URL = "http://localhost:8123"
HA_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2NDY5ZDU5ODI2ZjM0ZDUwOGQ5ZDc1ZmFiYjVkZTNmYyIsImlhdCI6MTc4NDMwMTEzMiwiZXhwIjoyMDk5NjYxMTMyfQ.-XMAmJTHnTXx5A_p2YOhna6yFgBy4dAfxAS2c8PYOMM"

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json"
}

# Wir fragen die API nach ALLES, was mit Wetter zu tun hat
url = f"{HA_URL}/api/states"
response = requests.get(url, headers=HEADERS, timeout=5)

if response.status_code == 200:
    entities = response.json()
    weather_entities = [e["entity_id"] for e in entities if e["entity_id"].startswith("weather.")]
    print("Gefundene Wetter-Entitäten in deinem Home Assistant:")
    print(weather_entities)
else:
    print(f"Fehler beim Verbinden mit Home Assistant. Status Code: {response.status_code}")

