def is_device_command(text):
    t = text.lower()
    return any(w in t for w in ["licht", "lampe", "schalte", "mach"])


def is_simple(text):
    return text.lower() in ["hallo", "hi", "hey"]


def is_knowledge_question(text):
    t = text.lower()
    return any(w in t for w in [
        "wie groß", "wer war", "was ist", "wann", "wo", "was frisst"
    ])


def route(text):
    t = text.lower()

    if is_device_command(t):
        return "device"

    if is_simple(t):
        return "simple"

    if is_knowledge_question(t):
        return "knowledge"

    return "llm"
