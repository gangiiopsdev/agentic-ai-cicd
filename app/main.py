from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

def safe_ping(host):
    try:
        # Safe implementation using subprocess.run with shell=False and proper argument passing
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    parsed_url = urlparse(host)
    if not parsed_url.hostname:
        raise ValueError("Invalid hostname")
    return safe_ping(parsed_url.hostname)