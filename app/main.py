from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and explicit arguments
    result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.strip().isalnum() or '.' in host:
        raise ValueError('Invalid host parameter')
    result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}