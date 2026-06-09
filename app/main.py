from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it's a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError('Invalid host format')
    subprocess.run(['ping', '-c 1', host], check=True, shell=False)
    return {"status": "completed"}