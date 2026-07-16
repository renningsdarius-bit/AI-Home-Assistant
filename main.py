from router import route
from actions import turn_on, turn_off
from llm import ask_llm
from knowledge import get_knowledge

# TODO: Router verbessern, "licht" triggert aktuell auch bei "Wie funktioniert Licht?"

print(" Assistant Core gestartet")

while True:
    text = input("Du: ")

    mode = route(text)

    if mode == "device":

        if "an" in text.lower():
            turn_on("light.livingroom")
            print("KI: Licht eingeschaltet")

        elif "aus" in text.lower():
            turn_off("light.livingroom")
            print("KI: Licht ausgeschaltet")

    elif mode == "simple":
        print("KI: Hallo 👋")

    elif mode == "knowledge":

        context = get_knowledge(text)

        prompt = f"""
Kontext:
{context}

Frage:
{text}

Antworte kurz und korrekt.
"""

        answer = ask_llm(prompt)
        print("KI:", answer)

    elif mode == "llm":

        answer = ask_llm(text)
        print("KI:", answer)
