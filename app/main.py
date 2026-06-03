from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    # Add your validation logic here (e.g., allowed IP ranges)
    if not host.isdigit():
        raise ValueError('Invalid host input')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    command = shlex.split(f'ping {host}')
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {'status': result.stdout}