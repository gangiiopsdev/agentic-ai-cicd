from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.replace('.', '').isdigit():
        return {"status": "error", "output": "Invalid host format."}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}  # Return the output for debugging purposes
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}