def is_device_command(text):
    t = text.lower()
    # evtl. anpassung der keywords notwendig
    return any(w in t for w in ["licht", "lampe", "steckdose", "schalte", "mach"])


def is_simple(text):
    return text.lower() in ["hallo", "hi", "hey", "hallo kumpel"]


def is_weather_question(text):
    t = text.lower()
    return any(w in t for w in ["wetter", "temperatur", "grad", "regnet", "sonne"])


def is_knowledge_question(text):
    t = text.lower()
    return any(w in t for w in [
        "wie groß", "wer war", "was ist", "wann", "wo", "was frisst"
    ])


def route(text):
    t = text.lower()

    # Wetter als eigene Route abfangen
    if is_weather_question(t):
        return "weather"

    if is_device_command(t):
        return "device"

    if is_simple(t):
        return "simple"

    if is_knowledge_question(t):
        return "knowledge"

    return "llm"
