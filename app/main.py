from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to only allow specific characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host parameter")
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}