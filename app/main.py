from fastapi import FastAPI
import subprocess
import re

def sanitize_host(host):
    return re.sub(r'[^a-zA-Z0-9.-]+', '', host)

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input
    sanitized_host = sanitize_host(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        raise ValueError("Invalid hostname")

    # Secure implementation
    subprocess.run(['ping', '-c 1', sanitized_host], check=True, shell=False)
    return {"status": "completed"}