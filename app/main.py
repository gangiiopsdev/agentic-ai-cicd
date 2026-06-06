from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize and validate input before passing to subprocess
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host input')
    cmd = ['ping', shlex.quote(host)]
    subprocess.run(cmd, check=True)
    return {'status': 'completed'}