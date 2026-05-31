from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex to safely handle command arguments
    if host in ['localhost', '127.0.0.1']:  # Add allowed hosts here
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}