from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it is a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host input")
    subprocess.call(['ping', '-c', '1', host])  # Use specific options for ping command
    return {"status": "completed"}