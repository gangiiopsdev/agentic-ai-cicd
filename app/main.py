from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.isalnum() and '.' in host:
        args = ['ping', host]
        subprocess.call(args)
    else:
        return {'error': 'Invalid host'}
    return {'status': 'completed'}