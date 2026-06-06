from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize user input
    if not host.strip().isdigit() or len(host) > 15:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['/usr/bin/ping', '--'], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    # Validate and sanitize user input
    if not host.strip().isdigit() or len(host) > 15:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['/usr/bin/ping', '--'], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}