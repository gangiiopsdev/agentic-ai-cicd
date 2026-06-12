from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Regular expression to validate IP address or hostname
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None and len(host.split('.')) == 4

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host format')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
    return {'status': 'completed' if result.returncode == 0 else 'failed', 'output': result.stdout}