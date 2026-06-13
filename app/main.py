from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if host.startswith('192.168.') or host.startswith('172.16.'):  # Example IP restrictions
        subprocess.call(['ping', host])
    else:
        return {'status': 'invalid host'}
    return {'status': 'completed'}