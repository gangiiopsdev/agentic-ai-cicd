from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "invalid_host"}
    # Secure implementation using list for command arguments
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}