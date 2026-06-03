from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return 'localhost' in host or '127.0.0.1' in host

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    command = ['ping', host]
    subprocess.call(command)
    return {'status': 'completed'}