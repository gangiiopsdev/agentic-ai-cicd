from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    cmd = ['ping', host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout.strip()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout.strip()}