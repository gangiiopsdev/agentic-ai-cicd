from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with validation and sanitization
    if not host.isdigit() or len(host) != 3:
        return {'status': 'error', 'reason': 'Invalid host parameter'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}