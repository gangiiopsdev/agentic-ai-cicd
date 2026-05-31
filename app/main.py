from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with validation and quoting
    if not host.isalnum():
        raise ValueError('Invalid input')
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True, timeout=5)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}