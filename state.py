STATE = {
    "lights": {},
    "sensors": {},
    "context": {
        "last_intent": None,
        "last_device": None,
        "last_action": None
    }
}

def set_context(key, value):
    STATE["context"][key] = value

def get_context(key):
    return STATE["context"].get(key)

def update_light(device, state):
    STATE["lights"][device] = state

def get_light(device):
    return STATE["lights"].get(device)
