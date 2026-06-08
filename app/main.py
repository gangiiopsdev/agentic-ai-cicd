from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation for host parameter
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}