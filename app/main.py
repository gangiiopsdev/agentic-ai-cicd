from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
global host

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    global host
    host = request.host.strip()
    if not host:
        raise ValueError('Host cannot be empty')
    safe_host = subprocess.list2cmdline([host])  # Sanitize the host input
    subprocess.run(['ping', '-c', '1', safe_host], check=True)
    return {"status": "completed", "host": host}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}