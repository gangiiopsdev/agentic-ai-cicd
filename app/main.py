from fastapi import FastAPI
import subprocess
from re import match

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not match(r'^[a-zA-Z0-9-. _]+$', host):
        return {"status": "error", "message": "Invalid host name"}
    result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}