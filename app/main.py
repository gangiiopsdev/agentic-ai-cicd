from fastapi import FastAPI
import subprocess
import shlex

cmd = ['ping', shlex.quote(host)]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(cmd, check=True)
    return {'status': 'completed'}