from fastapi import FastAPI
import subprocess
import re

def validate_host(host: str):
    # Simple regex to check for valid IP addresses and domain names
    pattern = r'^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|[a-zA-Z0-9.-]+)$'
    return re.match(pattern, host) is not None

def safe_ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)