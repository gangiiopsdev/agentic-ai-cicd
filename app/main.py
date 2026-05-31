from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip() or not host.isalnum():
        return {'error': 'Invalid host name'}
    try:
        subprocess.run(shlex.split(f'ping {host}'), check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}