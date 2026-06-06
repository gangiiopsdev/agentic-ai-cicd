from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to avoid shell injection
    if not host.strip().isalnum() and '-' not in host:
        raise ValueError('Invalid host name')
    command = ['ping', host]
    result = subprocess.run(shlex.split(' '.join(command)), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}