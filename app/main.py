from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Enhanced validation to ensure the host does not contain any shell metacharacters or control characters
    if not re.match(r'^[a-zA-Z0-9]*$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)