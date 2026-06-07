from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host input')
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {'status': 'completed'}