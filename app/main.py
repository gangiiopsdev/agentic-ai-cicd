from fastapi import FastAPI
import subprocess
import shlex
from urllib.parse import urlparse

app = FastAPI()

def validate_host(host):
    try:
        result = urlparse('http://' + host)
        return all(c.isalnum() or c in '-.' for c in result.netloc)
    except ValueError:
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed", "error": "Invalid host input"}