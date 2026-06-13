from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isnumeric():
        return False
    subprocess.call(f'ping {host}')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}