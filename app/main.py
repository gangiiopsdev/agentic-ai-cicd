from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host input")
    # Secure implementation using subprocess.run with shell=False and args tuple
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
    return {"status": "completed"}