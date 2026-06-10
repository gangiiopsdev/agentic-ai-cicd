from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.strip().isalnum() and '.' in host:
        args = ['ping', host]
        subprocess.call(args)
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}