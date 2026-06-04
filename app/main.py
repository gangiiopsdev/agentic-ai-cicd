from fastapi import FastAPI
import subprocess
from sanic.response import json

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host input to prevent command injection
    allowed_hosts = ['google.com', 'example.com']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return json(result.stdout)
        except subprocess.CalledProcessError as e:
            return json({'error': e.stderr}, status=500)

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)