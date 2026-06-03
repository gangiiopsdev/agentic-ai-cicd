from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize input
    if not host or not all(c.isalnum() for c in host) or len(host) > 255:
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)