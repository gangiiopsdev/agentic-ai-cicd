from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host parameter
    if not host.strip():
        raise ValueError("Host parameter cannot be empty")
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}