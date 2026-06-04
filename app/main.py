from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if host.isalnum() and len(host) <= 15:
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}