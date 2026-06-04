from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

def is_valid_host(host: str) -> bool:
    # Add your validation logic here
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None  # Basic regex to allow alphanumeric characters and some special characters