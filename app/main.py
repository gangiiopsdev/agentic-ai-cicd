from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the host parameter
    if not host.isalnum():
        return {"status": "invalid_host"}
    subprocess.call(['ping', host])
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)