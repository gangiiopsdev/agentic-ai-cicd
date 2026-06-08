from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    # Validate the input further or use a whitelist of allowed hosts
    if host not in ['allowed_host1', 'allowed_host2']:
        return {'status': 'error', 'message': 'Host not allowed'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    # Validate the input further or use a whitelist of allowed hosts
    if host not in ['allowed_host1', 'allowed_host2']:
        return {'status': 'error', 'message': 'Host not allowed'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}