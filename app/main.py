from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and proper use of subprocess
    if host.startswith('192.168.') or host.startswith('10.0.0.'):
        command = ['ping', host]
        subprocess.run(command, check=True)
    else:
        return {'error': 'Invalid host'}
    return {'status': 'completed'}