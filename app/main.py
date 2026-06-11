from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if not host.isalnum() and not all(c in '-.' for c in host):
        raise ValueError("Invalid host name")
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum() and not all(c in '-.' for c in host):
        raise ValueError("Invalid host name")
    subprocess.call(['ping', host])
    return {"status": "completed"}