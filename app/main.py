from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping_path = "/usr/bin/ping"  # Specify the full path to ping to avoid PATH issues

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    subprocess.run([ping_service.ping_path, host], check=True, text=True)
    return {"status": "completed"}