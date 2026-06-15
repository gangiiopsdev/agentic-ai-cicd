from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host or not host.isalnum():
        return {'status': 'invalid host'}
    command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}