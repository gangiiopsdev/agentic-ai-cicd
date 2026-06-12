from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's a valid hostname
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

def validate_host(host: str) -> bool:
    import socket
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False