from fastapi import FastAPI
import subprocess
import shlex
import re

def safe_ping(host: str):
    # Enhanced validation to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Simplified regex for demonstration purposes
        raise ValueError("Invalid hostname")
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host to ensure it is a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Enhanced regex for security
        raise ValueError("Invalid hostname")
    return safe_ping(host)