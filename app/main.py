from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

def safe_ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    return safe_ping(host)

import re
def is_safe_host(host: str) -> bool:
    # Improved regex to allow only alphanumeric and some special characters
    pattern = r'^[a-zA-Z0-9.-]+$'
    parsed_url = urlparse(host)
    return re.match(pattern, parsed_url.netloc) is not None