from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call and avoiding shell=True for security reasons.
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure the host is a valid IP address or hostname before using it in subprocess.run
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

import re
def is_valid_host(hostname: str) -> bool:
    # Simple regex to check for valid IP address or hostname
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, hostname) is not None