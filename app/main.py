from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if host.startswith('127.0.0.1') or host.startswith('localhost'):
        subprocess.call(args)
    else:
        return {'status': 'failed', 'message': 'Invalid host'}
    return {'status': 'completed'}