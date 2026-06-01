from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize user input to prevent command injection
    if not host or len(host) > 255:
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}