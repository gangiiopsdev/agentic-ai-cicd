from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 50:
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(['ping', host])
    return {"status": "completed"}