from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe for ping command
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host format")
    escaped_host = subprocess.quote(host)
    try:
        result = subprocess.run(["ping", escaped_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}