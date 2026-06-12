from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        pass

    @staticmethod
def ping(host: str):
        # Secure implementation
        args = ["ping", host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    safe_ping_instance = SafePing()
    return safe_ping_instance.ping(host)