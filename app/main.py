from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/"")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: Optional[str] = None):
    if not host:
        return {'status': 'failed', 'error': 'No host provided'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}

# Remediation: Validate and sanitize the input to prevent command injection.
def is_safe_host(host):
    # Add your validation logic here
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: Optional[str] = None):
    if not host or not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid or no host provided'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}