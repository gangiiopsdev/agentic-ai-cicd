from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Input validation to ensure only valid hostnames/IPs are processed
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid hostname/IP'}
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)
    return {'status': 'completed'}

def validate_host(host: str) -> bool:
    # Implement a simple validation logic
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)