from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = shlex.split('ping ' + shlex.quote(host))
    subprocess.run(args, check=True, capture_output=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    safe_ping(host)
    return {'status': 'completed'}