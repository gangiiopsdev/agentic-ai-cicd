from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    try:
        # Secure implementation using subprocess.run with sanitized input
        result = subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Validate host input to ensure it is a valid hostname or IP address
    if not re.match(r"^[a-zA-Z0-9.-]+$", host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    return ping(host)