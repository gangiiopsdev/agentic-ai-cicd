from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation to prevent command injection
    if not host.isalnum() or len(host) > 100:
        raise ValueError("Invalid host parameter")
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}