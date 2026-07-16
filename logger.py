from datetime import datetime

def log(event_type, message):
    line = f"[{datetime.now()}] [{event_type}] {message}"
    print(line)

    with open("assistant.log", "a") as f:
        f.write(line + "\n")
