from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/`")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    if '127.0.0.1' in host or 'localhost' in host:
        subprocess.call(["ping", host])
    else:
        return {"status": "Invalid host"}
    return {"status": "completed"}