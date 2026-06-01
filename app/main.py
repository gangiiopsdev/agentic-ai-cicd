from fastapi import FastAPI
import subprocess

cimport = subprocess.run

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        cimport(['ping', host], capture_output=True, text=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host specified'}