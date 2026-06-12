from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        return {'error': 'Invalid host'}, 400
    subprocess.run(shlex.split(f'ping {host}'), check=True)
    return {'status': 'completed'}