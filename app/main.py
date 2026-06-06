from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        raise ValueError('Invalid hostname')
    # Use a whitelist of allowed hosts to prevent command injection
    allowed_hosts = {'google.com', 'example.com'}
    if host not in allowed_hosts:
        raise ValueError('Hostname is not allowed')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping(host)