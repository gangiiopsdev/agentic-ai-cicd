from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping = 'ping'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str, ping_service=PingService()):
    result = subprocess.run([ping_service.ping, host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}