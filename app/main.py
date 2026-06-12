from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host or not host.isalnum():
        return {'status': 'invalid host'}
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True, shell=False)
    return {'status': 'completed'}