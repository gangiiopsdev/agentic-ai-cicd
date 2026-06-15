from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class SafePing:
    def __init__(self):
        self.ping_command = ['ping', '-c', '4']

class HostRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.post("/ping")
def ping(host_request: HostRequest):
    safe_ping = SafePing()
    # Using subprocess.run with a list to avoid shell injection
    result = subprocess.run(safe_ping.ping_command + [host_request.host], check=True, text=True)
    return {"status": "completed", "output": result.stdout}