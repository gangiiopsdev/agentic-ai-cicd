from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if host.isalnum() and len(host) < 50:
        subprocess.call(["ping", host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host parameter"}