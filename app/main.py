from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host parameter
    if not is_valid_host(host):
        raise ValueError('Invalid host parameter')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}

# Function to validate host parameter
import re
def is_valid_host(host: str) -> bool:
    # Regex pattern for a simple hostname or IP address validation
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None