import os
from gtts import gTTS

def sprich(text):
    tts = gTTS(text=text, lang='de', slow=False)
    tts.save("antwort.mp3")
    os.system("mpg123 antwort.mp3")
    os.remove("antwort.mp3")

sprich("Hallo! Der Sound funktioniert. Jetzt fehlen nur noch die Modelle.")
