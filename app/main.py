from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex to check for allowed characters and formats
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None