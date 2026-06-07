from fastapi import FastAPI
import subprocess
import re

# Regular expression to validate the host input
def validate_host(host: str):
    pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(pattern, host):
        raise ValueError("Invalid host")

app = FastAPI()
@app.get="/ping")
def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    validate_host(host)
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}