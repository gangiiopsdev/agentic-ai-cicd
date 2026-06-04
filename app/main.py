from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if not host.isalnum() or len(host) > 64:
        return {"status": "error", "message": "Invalid host name"}
    subprocess.call(["ping", host])
    return {"status": "completed"}