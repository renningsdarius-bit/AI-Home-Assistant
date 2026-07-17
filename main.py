import speech_recognition as sr
import pyttsx3
from router import route
# HIER get_weather hinzugefügt:
from actions import turn_on, turn_off, get_weather
from llm import ask_llm
from knowledge import get_knowledge

# Sprachausgabe initialisieren
engine = pyttsx3.init()
engine.setProperty('rate', 150) # Geschwindigkeit (etwas langsamer ist verständlicher)
voices = engine.getProperty('voices')
# Versuchen, eine deutsche Stimme zu setzen
for voice in voices:
    if "de" in voice.languages or "German" in voice.name:
        engine.setProperty('voice', voice.id)
        break

def sprich(text):
    print(f"KI: {text}")
    engine.say(text)
    engine.runAndWait()

print(" Assistant Core gestartet")
def lausche():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("\nIch höre zu...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="de-DE")
        print(f"Du: {text}")
        return text
    except:
        return ""

while True:
    text = lausche()
    if not text:
        continue

    mode = route(text)

    # HIER den neuen Block für das Wetter eingefügt:
    if mode == "weather":
        wetter_info = get_weather()
        # Wir lassen die KI den Satz direkt aussprechen, den HA liefert:
        sprich(wetter_info)

    elif mode == "device":
        if "an" in text.lower():
            turn_on("light.livingroom")
            sprich("Licht eingeschaltet")
        elif "aus" in text.lower():
            turn_off("light.livingroom")
            sprich("Licht ausgeschaltet")

    elif mode == "simple":
        sprich("Hallo! Wie kann ich dir helfen?")

    elif mode == "knowledge":
        context = get_knowledge(text)
        prompt = f"Kontext:\n{context}\n\nFrage:\n{text}\n\nAntworte kurz und korrekt."
        answer = ask_llm(prompt)
        sprich(answer)

    elif mode == "llm":
        answer = ask_llm(text)
        sprich(answer)
