from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent shell injection
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}