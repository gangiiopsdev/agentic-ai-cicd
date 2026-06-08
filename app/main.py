from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.replace('.', '').isnumeric() or len(host.split('.')) != 4:
        raise ValueError('Invalid IP address')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }