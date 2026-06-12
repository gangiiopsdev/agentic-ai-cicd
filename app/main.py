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
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    # Enhanced validation logic (e.g., check for allowed domains, IPs, etc.)
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None