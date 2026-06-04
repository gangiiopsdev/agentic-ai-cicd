from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run and args instead of shell=True
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid command injection
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        safe_ping(host)
    else:
        return {"status": "denied", "message": "Invalid host"}
    return {"status": "completed"}