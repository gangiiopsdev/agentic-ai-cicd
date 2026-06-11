from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific hostnames or IP addresses
    allowed_hosts = ['localhost', '127.0.0.1']
    return any(host.startswith(allowed) for allowed in allowed_hosts)