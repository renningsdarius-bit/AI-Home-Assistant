import requests
from logger import log

HA_URL = "http://localhost:8123"
HA_TOKEN = "DEIN_TOKEN"

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json"
}
# TODO: Später SSL/HTTPS einrichten, wenn HA von außen erreichbar ist

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
