import requests

MODEL = "qwen2.5:3b-instruct"

def ask_llm(question, context=""):
    try:
        r = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": "Antworte kurz und korrekt."},
                    {"role": "user", "content": question + "\n\n" + context}
                ],
                "stream": False
            },
            timeout=120
        )

        print("DEBUG STATUS:", r.status_code)
        print("DEBUG RAW:", r.text)

        data = r.json()
        return data["message"]["content"]

    except Exception as e:
        print("LLM ERROR:", e)
        return "LLM Fehler"
