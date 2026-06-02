from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    if host.strip().isalnum() and len(host) < 256:
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid hostname"}