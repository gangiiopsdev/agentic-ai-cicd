from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with proper validation
    if host.strip() and all(c.isalnum() or c in ['-', '.'] for c in host):
        subprocess.call(['ping', host])
    else:
        return {"status": "error", "message": "Invalid host name"}
    return {"status": "completed"}