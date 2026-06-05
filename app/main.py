from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip() and all(c.isalnum() or c in ['.', '-'] for c in host) and re.match(r'^[a-zA-Z0-9.-]+$', host):
        subprocess.run(['ping', host], check=True, shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid hostname"}