from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

global_host = 'example.com' # Ensure this is sanitized

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")

    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}