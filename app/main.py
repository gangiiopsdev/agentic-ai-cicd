from fastapi import FastAPI
import subprocess
import shlex
from urllib.parse import urlparse

global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    try:
        parsed_url = urlparse(host)
        if not all(c.isalnum() or c in '.-' for c in host) or parsed_url.scheme != '':
            return {"status": "failed", "error": "Invalid host name"}
        command = ['ping', '-c 1'] + shlex.split(host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}