from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.startswith('192.168.'):
        raise ValueError('Invalid host IP address')
    subprocess.call(['ping', host])
    return {'status': 'completed'}