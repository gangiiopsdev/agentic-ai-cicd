from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not all(c.isalnum() for c in host):
        return {'error': 'Invalid host'}, 400
    command = ['ping', quote(host)]
    subprocess.run(command, check=True, shell=False)
    return {'status': 'completed'}