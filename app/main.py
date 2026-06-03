from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isalnum() and len(host) <= 32:
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}