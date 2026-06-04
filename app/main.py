from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with input validation
    if not host.strip() or len(host) > 255:
        return {'status': 'invalid_host'}
    cmd = ['ping', shlex.quote(host)]
    subprocess.call(cmd)
    return {'status': 'completed'}