from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to ensure it does not contain potentially dangerous characters
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {"error": "Invalid host"}
    subprocess.call(['ping', host])
    return {"status": "completed"}