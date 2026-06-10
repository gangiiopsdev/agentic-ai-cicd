from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        safe_command = ['ping', host]
        result = subprocess.run(safe_command, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/"}
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    response = SafePing.ping(host)
    return {"status": "completed", "response": response}