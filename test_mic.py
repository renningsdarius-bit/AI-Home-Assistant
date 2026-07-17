import speech_recognition as sr

r = sr.Recognizer()

# Python soll standard Mikrofon nutzen
with sr.Microphone() as source:
    print("\n=== MIKROFON-TEST ===")
    print("Bitte warte kurz, Hintergrundgeräusche werden herausgefiltert...")
    r.adjust_for_ambient_noise(source, duration=2)

    print("\nBereit! Sprich jetzt etwas (z.B. 'Hallo Pi')...")
    audio = r.listen(source)

try:
    print("Verarbeite Audio...")
    # Audio wird an Erkennung geschickt
    text = r.recognize_google(audio, language="de-DE")
    print(f"\nErfolgreich erkannt: '{text}'")
except sr.UnknownValueError:
    print("\nSchade: Audio wurde aufgenommen, aber ich konnte keine Wörter verstehen.")
except sr.RequestError as e:
    print(f"\nFehler: Konnte keine Verbindung zum Dienst aufbauen ({e})")
