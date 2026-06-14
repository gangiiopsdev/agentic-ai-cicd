from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', '-c', '4']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    # Using subprocess.run with a list to avoid shell injection
    result = subprocess.run(safe_ping.ping_command + [host], check=True, text=True)
    return {"status": "completed", "output": result.stdout}