from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host to ensure it's a safe IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host provided')
    subprocess.run(['ping', '-c', '1', host], check=True, timeout=5)
    return {'status': 'completed'}