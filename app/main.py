from fastapi import FastAPI
import subprocess
import shlex
global host_whitelist = {'google.com', 'example.com'}
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if not host or host.strip() == '':
        raise ValueError('Host is required')
    if host not in host_whitelist:
        raise ValueError('Host is not allowed')
    # Secure implementation using subprocess.run
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}