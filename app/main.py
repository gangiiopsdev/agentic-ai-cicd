from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host parameter
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}