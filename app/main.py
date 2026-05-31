from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', 'example.com']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    safe_host = host.strip()
    if len(safe_host) > 0 and all(c.isalnum() or c in '-.' for c in safe_host):
        subprocess.call(['ping', safe_host])
    return {"status": "completed"}