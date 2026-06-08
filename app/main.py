from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping_safe(host: str):
    # Enhanced validation to allow only alphanumeric characters and hyphens
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    try:
        return ping_safe(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}