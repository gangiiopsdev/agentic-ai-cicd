from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/"}
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}