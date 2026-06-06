from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Regular expression to allow only alphanumeric characters and hyphens in hostnames/IP addresses
ALLOWED_HOST_PATTERN = re.compile(r'^[a-zA-Z0-9-]+$')

def ping(host: str):
    if not ALLOWED_HOST_PATTERN.match(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)